def find_virtual_service(vs_list, name):
     for vs in vs_list:
          print(" -", vs["name"])
          if vs["name"] == name:
               return vs
     return None


def validate_enabled(vs, expected=True):
     if vs["enabled"] != expected:
          raise Exception(f"Validation failed: enabled={vs['enabled']}")
     print(f"[VALIDATION] enabled={vs['enabled']} ✓")
