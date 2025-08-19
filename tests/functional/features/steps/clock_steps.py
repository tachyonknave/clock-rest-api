
import requests
from behave import given, when, then
from behave.runner import Context
from fixtures import test_program

@given("the Clock Rest API is running")
def given_the_clock_rest_api_is_running(context: Context):
    pass


@when("the health endpoint is accessed")
def when_the_health_endpoint_is_accessed(context: Context):
    response = requests.get(context.base_url + context.health_endpoint)
    context.response_text = response.text.strip()


@then("we get an okay response")
def then_we_get_an_okay_response(context: Context):
    print(context.response_text)
    assert context.response_text == '"OK"', 'Expecting "OK"'

# Scenario: Save a program
#  Given the Clock Rest API is running
#  When we provide a test program to the api
#  Then we get a created response

@when("we provide a test program to the api")
def we_provide_a_test_program(context: Context):
    response = requests.post(context.base_url + context.program_endpoint,
                            data=test_program())
    context.response_code = response.status_code

@then("we get a created response")
def then_we_get_a_created_response(context: Context):
    assert context.response_code == 201, f"Expected status code: 201, Actual: {context.response_code}"
