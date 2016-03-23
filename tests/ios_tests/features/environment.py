import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if not path in sys.path:
    sys.path.insert(0, path)
from lib.appium_starter import start_appium, stop_appium
from lib.create_driver import create_driver
from lib.configuration_reader import load_configuration_from_file
from lib.logger import Logger
from lib.ios_commands import Commands

cmd = Commands()
log = Logger()
CONFIG = load_configuration_from_file('ios_config.json')

def before_all(context):
    log.logger('DEBUG', 'Executing after all\n')
    tags = CONFIG["APPIUM_TAGS"]
    start_appium(str(tags))


def before_feature(context, feature):
    log.logger('DEBUG', 'Before feature\n')
    context.driver = create_driver('ios', reinstallApp=True)


def before_scenario(context, scenario):
    log.logger('DEBUG', 'Before scenario\n')
    logs_file = scenario.__dict__['name'].replace(' ', '') + '.log'
    cmd.start_ios_logs(logs_file)
    context.driver.close_app()
    context.driver.launch_app()


def after_scenario(context,scenario):
    log.logger('DEBUG', 'After scenario\n')
    if context.failed:
        screenshot = scenario.__dict__['name'].replace(' ', '') + '.png'
        cmd.take_scrennshot(screenshot)
    context.driver.close_app()
    cmd.stop_ios_logs()


def after_feature(context,feature):
    log.logger('DEBUG', 'After feature\n')
    context.driver.quit()


def after_all(context):
    log.logger('DEBUG', 'Executing after all\n')
    stop_appium()