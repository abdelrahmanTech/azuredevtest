import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/predict")

    def on_start(self):
        self.client.post("/predict", json={"username":"foo", "password":"bar"})
        host = 'https://mlazurewebap.azurewebsites.net/'