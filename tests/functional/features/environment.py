from behave.runner import Context


def before_all(context: Context):
    context.base_url = "http://localhost:5001/"

    context.health_endpoint = "health"
    context.clock_endpoint = "clock"
