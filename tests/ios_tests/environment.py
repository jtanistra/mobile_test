import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if not path in sys.path:
    sys.path.insert(0, path)
from lib.appium_starter import start_appium, stop_appium
from lib.create_driver import create_driver
from lib.configuration_reader import load_configuration_from_file

CONFIG = load_configuration_from_file('iso_config.json')

def before_all(context):
    tags = CONFIG["APPIUM_TAGS"]
    start_appium(str(tags))


def before_feature(context, feature):
    print("Before feature\n")
    context.driver = create_driver('ios', reinstallApp=True)


def before_scenario(context, scenario):
    print("Before scenario\n")
    context.driver.close_app()
    context.driver.launch_app()


def after_scenario(context,scenario):
    print("After scenario\n")
    context.driver.close_app()


def after_feature(context,feature):
    context.driver.quit()
    print("\nAfter feature")


def after_all(context):
    print("Executing after all\n")
    stop_appium()