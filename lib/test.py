from datetime import datetime
from time import sleep

androidBluetoothSwitchId = "com.android.settings:id/switch_widget"
androidBarId = "android:id/statusBarBackground"
androidHeaderId = "com.android.systemui:id/header"
androidSettingsButtonId = "com.android.systemui:id/settings_button"
androidBluetoothMenuName = "Bluetooth"
killTaskButtonId = "com.android.systemui:id/dismiss_task"


def getBTswitchObject(driver):
    return driver.find_element_by_id(androidBluetoothSwitchId)


def isBTswithChecked(driver):
    status = getBTswitchObject(driver).get_attribute("checked")
    if status == "true":
        return True
    else:
        return False

def expandHeader(driver):
    driver.find_element_by_id(androidHeaderId).click()

def clickBTMenu(driver):
    driver.find_element_by_name(androidBluetoothMenuName).click()

def clickOptionsButton(driver):
    driver.find_element_by_id(androidSettingsButtonId).click()

def resetBT(driver):
    expandUpperBar(driver)
    expandHeader(driver)
    clickOptionsButton(driver)
    clickBTMenu(driver)
    if not isBTswithChecked(driver):
        print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Bluetooth was turned off")
    else:
        getBTswitchObject(driver).click()
        sleep(0.5)
        if not isBTswithChecked(driver):
           print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Bluetooth turned off")
        else:
            raise AssertionError("[ERROR] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Turning off BT failed")
    getBTswitchObject(driver).click()
    sleep(4)
    if isBTswithChecked(driver):
       print("[LOG] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Bluetooth turned on")
    else:
        raise AssertionError("[ERROR] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Turning on BT failed")
    driver.back()
    driver.back()

def expandUpperBar(driver):
    scrennHeight = driver.get_window_size()['height']
    scrennWidth = driver.get_window_size()['width']
    bar = driver.find_element_by_id(androidBarId)
    driver.tap([[scrennWidth/2, 20]])
    sleep(0.1)
    driver.tap([[scrennWidth/2, 20]])
    # bar.click()
    # self.expandHeader()

# driver = lib.create_driver.create_driver('Android')



def start(driver):
    resetBT(driver)

# driver.quit()
