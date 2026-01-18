import requests

class ApiClient:
     def __init__(self, base_url, username, password):
          self.base_url = base_url
          self.token = self.login(username, password)

     def login(self, username, password):
          response = requests.post(
               f"{self.base_url}/login",
               auth=(username, password)
          )
          response.raise_for_status()
          return response.json()["token"]

     def headers(self):
          return {"Authorization": f"Bearer {self.token}"}

     def get(self, endpoint):
          return requests.get(
               f"{self.base_url}{endpoint}",
               headers=self.headers()
          ).json()

     def put(self, endpoint, payload):
          return requests.put(
               f"{self.base_url}{endpoint}",
               headers=self.headers(),
               json=payload
          ).json()
