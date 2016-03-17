import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..'))
if not path in sys.path:
    sys.path.insert(0, path)
from lib.appium_starter import start_appium, stop_appium
from lib.create_driver import create_driver
from lib.adb_commnads import adb_shell_screenrecord, adb_shell_screenrecord_stop, adb_pull, adb_logcat_android


def before_all(context):
    start_appium()


def before_feature(context, feature):
    context.driver = create_driver('android', reinstallApp=True)
    print("Before feature\n")


def before_scenario(context, scenario):
    adb_shell_screenrecord('/sdcard/Download')
    context.driver.close_app()
    context.driver.launch_app()
    print("Before scenario\n")


def after_scenario(context,scenario):
    print("After scenario\n")
    context.driver.close_app()

def after_feature(context,feature):
    context.driver.quit()
    print("\nAfter feature")


def after_all(context):
    print("Executing after all")
    stop_appium()