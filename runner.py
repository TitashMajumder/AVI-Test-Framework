import yaml
from concurrent.futures import ThreadPoolExecutor

from core.api_client import ApiClient
from core.prefetcher import prefetch_resources
from core.validator import find_virtual_service, validate_enabled
from core.executor import disable_virtual_service
from mocks.ssh import mock_ssh
from mocks.rdp import mock_rdp


def run_test(test_case, api):
    print(f"\n[TEST STARTED] {test_case['name']}")

    mock_ssh()
    mock_rdp()

    vs_list = prefetch_resources(api)

    vs = find_virtual_service(vs_list, test_case["target_vs_name"])
    if not vs:
        raise Exception("Target Virtual Service not found")

    validate_enabled(vs, True)

    disable_virtual_service(api, vs["uuid"])

    vs_after = api.get(f"/api/virtualservice/{vs['uuid']}")
    validate_enabled(vs_after, False)

    print(f"[TEST PASSED] {test_case['name']}")


def main():
    with open("config/api_config.yaml") as f:
        api_cfg = yaml.safe_load(f)

    with open("config/test_cases.yaml") as f:
        tests = yaml.safe_load(f)["test_cases"]

    api = ApiClient(
        api_cfg["base_url"],
        api_cfg["username"],
        api_cfg["password"]
    )

    with ThreadPoolExecutor(max_workers=2) as executor:
        for test in tests:
            executor.submit(run_test, test, api)


if __name__ == "__main__":
    main()
