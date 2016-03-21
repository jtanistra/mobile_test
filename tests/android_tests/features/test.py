from lib.configuration_reader import load_configuration_from_file

CONFIG = load_configuration_from_file('android_config.json')

print(str(CONFIG["APPIUM_TAGS"]))


