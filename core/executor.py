def disable_virtual_service(api, uuid):
     response = api.put(
          f"/api/virtualservice/{uuid}",
          {"enabled": False}
     )
     print("[EXECUTOR] Virtual Service disabled")
     return response
