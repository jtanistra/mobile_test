from behave import given, when, then, use_step_matcher
from lib.test import start

use_step_matcher("re")


@given("Start Page")
def step_impl(context):
    start(context.driver)
    print('GIVEN')
    assert True


@when("Click start button")
def step_impl(context):
    print('WHEN')
    assert True


@then("I can see")
def step_impl(context):
    print('THEN')
    assert True
