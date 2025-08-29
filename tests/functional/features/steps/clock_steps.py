import json

import requests
from behave import given, when, then
from behave.runner import Context

from fixtures.clock_commands import get_test_clock_command


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


@when("a test clock command is sent")
def when_a_test_command_is_sent(context: Context):
    test_data = get_test_clock_command()
    response = requests.post(
        url=context.base_url + context.clock_endpoint,
        headers={"Content-Type": "application/json"},
        data=json.dumps(test_data),
    )
    print(response.text)
    context.response_code = response.status_code


@then("we get a {response_code} response")
def then_we_get_an_okay_response(context: Context, response_code: int):
    assert context.response_code == int(
        response_code
    ), f"Expecting {response_code}, got {context.response_code}"
