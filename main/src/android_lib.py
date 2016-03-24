from lib.adb_commnads import adb_pull
from lib.configuration_reader import load_configuration_from_file
import os
from selenium.webdriver.common.by import By
from lib.driver_commands import DriverCommands
from lib.logger import Logger


class AndroidLib(Logger):

    def __init__(self, driver):
        self.driver = driver
        self.rec_path = load_configuration_from_file('android_config.json')['REC_PATH']
        self.logs_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/../logs/'
        self.dr_commands = DriverCommands(self.driver)
        self.android_settings_selector =  (By.ID, 'com.android.systemui:id/settings_button')
        self.android_bth_menu_selector = (By.NAME, 'Bluetooth')
        self.android_bth_switch_selector = (By.ID, 'com.android.settings:id/switch_widget')

    def get_recorded_test(self, file_name):
        """
        Function pull file from android device with recorded test and save it in project logs directory.
        :param file_name: file name to save
        """
        file = self.logs_path + file_name
        adb_pull(self.rec_path, file)
        self.logger('INFO', 'screen record saved in logs directory')

    def android_bar_expand(self, driver):
        """
        Function opens android task bar
        :param driver: Appium driver

        """
        driver.swipe(535,1, 535, 1000)
        driver.swipe(535,1, 535, 1000)
        self.logger('INFO', 'android upper bar opened')

    def settings_icon_click(self):
        """
        Function allows to open android settings
        """
        self.dr_commands.find_element(self.android_settings_selector).click()
        self.logger('INFO', 'android settings opened')

    def bth_menu_click(self):
        """
        function opens bluetooth settings details
        :return:
        """
        self.dr_commands.find_element(self.android_bth_menu_selector).click()
        self.logger('INFO', 'android bluetooth menu opened')

    def bth_is_enabled(self):
        """
        function checks bluetooth adapter states
        :return: Bool: True if bluetooth is enabled or False is not
        """
        state = self.dr_commands.find_element(self.android_bth_switch_selector).get_attribute('checked')
        if state == 'false':
            self.logger('INFO', 'Bluetooth is disabled')
            return False
        else:
            self.logger('INFO', 'Bluetooth is enabled')
            return True

    def _bth_switch_click(self):
        """
        Function change bluetooth adapter state to next one.
        """
        self.dr_commands.find_element(self.android_bth_switch_selector).click()

    def bth_enable(self):
        """
        function checks bluetooth state and turn it on if state is off
        """
        self.logger('INFO', 'Trying to enable bluetooth')
        state = self.bth_is_enabled()
        if state:
            self.logger('WARNING', 'Bluetooth is already enabled')
        else:
            self._bth_switch_click()
            self.logger('INFO', 'Bluetooth enabled')

    def bth_disable(self):
        """
        function checks bluetooth state and turn it off if state is on
        """
        self.logger('INFO', 'Trying disable bluetooth')
        state = self.bth_is_enabled()
        if state:
            self._bth_switch_click()
            self.logger('INFO', 'Bluetooth disabled')
        else:
            self.logger('WARNING',  'Bluetooth is already disabled')

    def bth_restart(self):
        """
        Functions turn off and turn on bluetooth adapter
        """
        self.bth_disable()
        self._bth_switch_click()
        self.logger('INFO', 'Adapter restarted')
