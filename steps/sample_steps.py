# sample_steps.py

import requests
from behave import given, when, then

API_BASE_URL = "https://reqres.in/api"

@given('a valid API endpoint for user retrieval')
def step_given_valid_api_endpoint(context):
    context.url = f"{API_BASE_URL}/users/1"

@when('a GET request is made')
def step_when_get_request(context):
    context.response = requests.get(context.url)

@then('the status code should be {expected_status}')
def step_then_status_code(context, expected_status):
    assert context.response.status_code == int(expected_status), f"Expected status code {expected_status}, but got {context.response.status_code}"

@then('the response message should contain "{expected_message}"')
def step_then_response_message(context, expected_message):
    assert expected_message in context.response.text, f"Expected message '{expected_message}' not found in response"
