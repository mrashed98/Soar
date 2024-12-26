from behave import given, when, then
import requests
from faker import Faker
import time
import concurrent.futures
import statistics

fake = Faker()

@given('the application is running')
def step_impl(context):
    try:
        response = requests.get(context.base_url)
        assert response.status_code == 200
    except:
        raise Exception("Application is not running")

@when('I send {num:d} registration requests with random data')
def step_impl(context, num):
    context.start_time = time.time()
    context.responses = []
    
    def send_request():
        data = {
            'fullName': fake.name(),
            'userName': fake.user_name(),
            'email': fake.email(),
            'password': fake.password(),
            'phone': fake.phone_number()
        }
        return requests.post(f"{context.base_url}/client_registeration", data=data)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        context.responses = list(executor.map(lambda _: send_request(), range(num)))
    
    context.duration = time.time() - context.start_time

@then('all requests should complete within {seconds:d} seconds')
def step_impl(context, seconds):
    assert context.duration < seconds, f"Requests took {context.duration} seconds"

@then('the success rate should be above {percentage:d}%')
def step_impl(context, percentage):
    success_count = sum(1 for r in context.responses if r.status_code == 200)
    success_rate = (success_count / len(context.responses)) * 100
    assert success_rate > percentage, f"Success rate was {success_rate}%"

@when('I send concurrent login requests with increasing load')
def step_impl(context):
    context.responses = []
    loads = [5, 10, 15, 20]  # Increasing load sizes
    
    def send_login_request():
        data = {
            'userName': fake.user_name(),
            'email': fake.email(),
            'password': fake.password()
        }
        return requests.post(f"{context.base_url}/client_login", data=data)
    
    for concurrent_users in loads:
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_users) as executor:
            batch_responses = list(executor.map(lambda _: send_login_request(), range(concurrent_users)))
            context.responses.extend(batch_responses)

@then('the response time should stay under {seconds:d} seconds')
def step_impl(context, seconds):
    response_times = [r.elapsed.total_seconds() for r in context.responses]
    avg_response_time = statistics.mean(response_times)
    assert avg_response_time < seconds, f"Average response time was {avg_response_time} seconds"

@then('the error rate should be below {percentage:d}%')
def step_impl(context, percentage):
    error_count = sum(1 for r in context.responses if r.status_code != 200)
    error_rate = (error_count / len(context.responses)) * 100
    assert error_rate < percentage, f"Error rate was {error_rate}%"
