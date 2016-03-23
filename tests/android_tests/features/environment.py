import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if not path in sys.path:
    sys.path.insert(0, path)
from lib.appium_starter import start_appium, stop_appium
from lib.create_driver import create_driver
from lib.adb_commnads import adb_shell_screenrecord, adb_logcat_android, adb_shell_screenrecord_stop
from lib.configuration_reader import load_configuration_from_file
from main.src.android_lib import AndroidLib
from behave.log_capture import capture

CONFIG = load_configuration_from_file('android_config.json')


def before_all(context):
    tags = CONFIG["APPIUM_TAGS"]
    start_appium(str(tags))
    context.config.setup_logging()


def before_feature(context, feature):
    print("Before feature\n")
    context.driver = create_driver('android', reinstallApp=True)


def before_scenario(context, scenario):
    print("Before scenario\n")
    adb_shell_screenrecord(CONFIG['REC_PATH'])
    adb_logcat_android(CONFIG['ANDROID_TAGS_ALL'])
    context.driver.close_app()
    context.driver.launch_app()


def after_scenario(context,scenario):
    print("After scenario\n")
    adb_shell_screenrecord_stop()
    if context.failed:
        context.andr_lib = AndroidLib(context.driver)
        movie_name = scenario.__dict__['name'].replace(' ', '') + '.mp4'
        print(scenario.__dict__['name'].replace(' ', ''))
        print(movie_name)
        context.andr_lib.get_recorded_test(movie_name.replace(' ', ''))
    context.driver.close_app()


def after_feature(context,feature):
    context.driver.quit()
    print("\nAfter feature")


def after_all(context):
    print("Executing after all\n")
    stop_appium()