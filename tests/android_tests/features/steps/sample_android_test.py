from behave import *
from main.src.android_lib import AndroidLib


use_step_matcher("re")


@then("TH")
def step_impl(context):
    andr.bth_menu_click()
    assert False


@given("GV")
def step_impl(context):
    global andr
    andr = AndroidLib(context.driver)
    andr.android_bar_expand(context.driver)


@when("WH")
def step_impl(context):
    andr.settings_icon_click()