from locust import HttpUser, task, between
from faker import Faker
import random

fake = Faker()

class PerformanceTest(HttpUser):
    wait_time = between(1, 3)  # Wait 1-3 seconds between tasks
    
    def on_start(self):
        self.client.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    @task(3)  # Weight of 3 for registration
    def test_registration(self):
        data = {
            'fullName': fake.name(),
            'userName': fake.user_name(),
            'email': fake.email(),
            'password': fake.password(),
            'phone': fake.phone_number()
        }
        self.client.post("/client_registeration", data=data)

    @task(2)  # Weight of 2 for login
    def test_login(self):
        data = {
            'userName': fake.user_name(),
            'email': fake.email(),
            'password': fake.password()
        }
        self.client.post("/client_login", data=data)
