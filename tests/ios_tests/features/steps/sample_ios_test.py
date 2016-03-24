from behave import *

use_step_matcher("re")


@given("ios given")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("ios when")
def step_impl(context):
    assert False

@then("ios then")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass