from behave import *
from main.src.android_lib import AndroidLib


use_step_matcher("re")


@then("TH")
def step_impl(context):
    pass


@given("GV")
def step_impl(context):
    andr = AndroidLib(context.driver)
    andr.expoand_android_bar(context.driver)
    andr.click_settings_icon(context.driver)


@when("WH")
def step_impl(context):
    pass