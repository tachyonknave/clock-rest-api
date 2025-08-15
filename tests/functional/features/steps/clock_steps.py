import requests
from behave import given, when, then
from behave.runner import Context


@given('the Clock Rest API is running')
def given_the_clock_rest_api_is_running(context: Context):
    pass

@when('the health endpoint is accessed')
def when_the_health_endpoint_is_accessed(context: Context):
    response = requests.get(context.base_url + context.health_endpoint)
    context.response_text = response.text.strip()

@then('we get an okay response')
def then_we_get_an_okay_response(context: Context):
    print(context.response_text)
    assert context.response_text == '"OK"', 'Expecting "OK"'
