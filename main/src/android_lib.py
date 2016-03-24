from lib.adb_commnads import adb_pull
from lib.configuration_reader import load_configuration_from_file
import os
from selenium.webdriver.common.by import By
from lib.driver_commands import DriverCommands

class AndroidLib():

    def __init__(self, driver):
        self.driver = driver
        self.rec_path = load_configuration_from_file('android_config.json')['REC_PATH']
        self.logs_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/../logs/'
        self.dr_commands = DriverCommands(self.driver)
        self.android_settings_selector = (By.ID, 'com.android.systemui:id/setting_button')
        self.android_bth_menu_selector = (By.NAME, 'Bluetooth')
        self.android_bth_switch_selector = (By.XPATH, '//android.widget.LinearLayout[3]/android.widget.Switch[1]')

    def get_recorded_test(self, file_name):
        """
        Function pull file from android device with recorded test and save it in project logs directory.
        :param file_name: file name to save
        """
        file = self.logs_path + file_name
        adb_pull(self.rec_path, file)
        print('INFO: screen record saved in logs directory')

    def android_bar_expand(self, driver):
        """
        Function opens android task bar
        :param driver: Appium driver

        """
        driver.swipe(535, 1, 535, 2)
        driver.swipe(535, 1, 535, 1000)
        #driver.swipe(535, 1, 535, 1000)
        print('INFO: android upper bar opened')

    def settings_icon_click(self):
        """
        Function allows to open android settings
        """
        self.dr_commands.find_element(self.android_settings_selector).click()
        print('INFO: android settings opened')

    def bth_menu_click(self):
        """
        function opens bluetooth settings details
        :return:
        """
        self.dr_commands.find_element(self.android_bth_menu_selector).click()
        print('INFO: android bluetooth menur opened')

    def bth_is_enabled(self):
        """
        function checks bluetooth adapter states
        :return: Bool: True if bluetooth is enabled or False is not
        """
        state = self.dr_commands.find_element(self.android_bth_switch_selector).get_attribute('checked')
        if state == 'false':
            return False
        else:
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
        print('INFO: Trying enable bluetooth')
        state = self.bth_is_enabled()
        if state:
            print('WARNING: Bluetooth is already enabled')
        else:
            self._bth_switch_click()
            print('INFO: Bluetooth enabled')

    def bth_disable(self):
        """
        function checks bluetooth state and turn it off if state is on
        """
        print("INFO: Trying disable bluetooth")
        state = self.bth_is_enabled()
        if state:
            self._bth_switch_click()
            print('INFO: Bluetooth disabled')
        else:
            print('WARNING: Bluetooth is already disabled')

    def bth_restart(self):
        """
        Functions turn off and turn on bluetooth adapter
        """
        self.bth_disable()
        self._bth_switch_click()
        print('INFO: Adapter restarted')





# from Appium.common.webdriverutil import *
# from datetime import datetime
# from time import sleep
# import subprocess

# class android:
#     def __init__(self, driver):
#         self.driver = driver
#
#         self.androidBarId = "android:id/statusBarBackground"
#         self.androidHeaderId = "com.android.systemui:id/header"
#         self.androidSettingsButtonId = "com.android.systemui:id/settings_button"
#         self.androidBluetoothMenuName = "Bluetooth"
#         self.androidBluetoothSwitchId = "com.android.settings:id/switch_widget"
#         self.killTaskButtonId = "com.android.systemui:id/dismiss_task"
#         self.scrennHeight = self.driver.get_window_size()['height']
#         self.scrennWidth = self.driver.get_window_size()['width']


#     def expandUpperBar(self):
#         bar = self.driver.find_element_by_id(self.androidBarId)
#         self.driver.tap([[self.scrennWidth/2, 20]])
#         sleep(0.1)
#         self.driver.tap([[self.scrennWidth/2, 20]])
#         # bar.click()
#         # self.expandHeader()
#
#     def expandHeader(self):
#         self.driver.find_element_by_id(self.androidHeaderId).click()
#
#     def clickOptionsButton(self):
#         self.driver.find_element_by_id(self.androidSettingsButtonId).click()
#
#     def clickBTMenu(self):
#         self.driver.find_element_by_name(self.androidBluetoothMenuName).click()
#
#     def getBTswitchObject(self):
#         return self.driver.find_element_by_id(self.androidBluetoothSwitchId)
#
#     def isBTswithChecked(self):
#         status = self.getBTswitchObject().get_attribute("checked")
#         if status == "true":
#             return True
#         else:
#             return False
#
#     def turnBTon(self):
#         self.expandUpperBar()
#         self.expandHeader()
#         self.clickOptionsButton()
#         self.clickBTMenu()
#         if self.isBTswithChecked():
#             print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Bluetooth was already turned on")
#         else:
#             self.getBTswitchObject().click()
#             sleep(4)
#             if self.isBTswithChecked():
#                print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Bluetooth turned on")
#             else:
#                 raise AssertionError("[ERROR] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Turning on BT failed")
#         self.driver.back()
#         self.driver.back()
#
#     def turnBToff(self):
#         self.expandUpperBar()
#         self.expandHeader()
#         self.clickOptionsButton()
#         self.clickBTMenu()
#         if not self.isBTswithChecked():
#             print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Bluetooth was already turned off")
#         else:
#             self.getBTswitchObject().click()
#             sleep(0.5)
#             if not self.isBTswithChecked():
#                print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Bluetooth turned off")
#             else:
#                 raise AssertionError("[ERROR] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Turning off BT failed")
#         self.driver.back()
#         self.driver.back()
#
#     def resetBT(self):
#         self.expandUpperBar()
#         self.expandHeader()
#         self.clickOptionsButton()
#         self.clickBTMenu()
#         if not self.isBTswithChecked():
#             print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Bluetooth was turned off")
#         else:
#             self.getBTswitchObject().click()
#             sleep(0.5)
#             if not self.isBTswithChecked():
#                print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Bluetooth turned off")
#             else:
#                 raise AssertionError("[ERROR] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Turning off BT failed")
#         self.getBTswitchObject().click()
#         sleep(4)
#         if self.isBTswithChecked():
#            print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Bluetooth turned on")
#         else:
#             raise AssertionError("[ERROR] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Turning on BT failed")
#         self.driver.back()
#         self.driver.back()
#
#
#     def openTaskSwitcher(self):
#         subprocess.call("adb shell input keyevent 187", shell=True)
#         print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Opened android Task Switcher")
#
#     def killAllTasks(self):
#         self.openTaskSwitcher()
#         allKilled = False
#         while not allKilled:
#             try:
#                 self.driver.find_element_by_id(self.killTaskButtonId).click()
#             except:
#                 allKilled = True
#         print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " All task were killed")
#
#     def isProcessRuning(self, name):
#         output = subprocess.check_output("adb shell ps " + name, shell=True)
#         if name in output:
#             return True
#         else:
#             return False
#
#     def adbKillProcess(self, name):
#         subprocess.call("adb shell am force-stop " + name, shell=True)
#
#     def isProcessKilled(self, name):
#         if self.isProcessRuning(name):
#             self.adbKillProcess(name)
#             raise AssertionError("[ERROR] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + \
#                                            " Process " + name + " is still running. Killed using adb")
#         else:
#             print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Process " + name + " was properly killed.")
#
#     def isProcessAlive(self, name):
#         if self.isProcessRuning(name):
#             self.adbKillProcess(name)
#             print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") +
#                   " Process " + name + " was properly alive. Killed using adb.")
#         else:
#             raise AssertionError("[ERROR] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + \
#                                            " Process " + name + " was not running")