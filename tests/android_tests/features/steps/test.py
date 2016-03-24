from behave import *
from main.src.android_lib import AndroidLib


use_step_matcher("re")


@then("TH")
def step_impl(context):
    pass


@given("GV")
def step_impl(context):
    andr = AndroidLib(context.driver)
    andr.android_bar_expand(context.driver)
    andr.settings_icon_click()
    andr._bth_switch_click()


@when("WH")
def step_impl(context):
    pass