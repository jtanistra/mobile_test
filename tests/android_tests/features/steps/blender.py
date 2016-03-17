from behave   import given, when, then
from hamcrest import assert_that, equal_to
import os
import sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..'))
if not path in sys.path:
    sys.path.insert(1, path)
from main.android.pages.blender import Blender

@given('I put "{thing}" in a blender')
def step_given_put_thing_into_blender(context, thing):
    context.blender = Blender()
    context.blender.add(thing)

@when('I switch the blender on')
def step_when_switch_blender_on(context):
    context.blender.switch_on()

@then('it should transform into "{other_thing}"')
def step_then_should_transform_into(context, other_thing):
    assert_that(context.blender.result, equal_to(other_thing))