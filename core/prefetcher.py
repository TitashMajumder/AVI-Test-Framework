def prefetch_resources(api):
     tenants = api.get("/api/tenant")["results"]
     virtual_services = api.get("/api/virtualservice")["results"]
     service_engines = api.get("/api/serviceengine")["results"]

     print(f"[PREFETCH] Tenants: {len(tenants)}")
     print(f"[PREFETCH] Virtual Services: {len(virtual_services)}")
     print(f"[PREFETCH] Service Engines: {len(service_engines)}")

     return virtual_services