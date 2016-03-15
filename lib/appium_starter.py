import subprocess
import os
from time import sleep
import datetime


def start_appium(*args):
    """
    Function starts appium server in subprocess
    :param args: appium server arguments according to appium documentation http://appium.io/slate/en/master/?python#appium-server-arguments
    """
    stop_appium()
    subprocess.Popen(
        ('appium', *args, '&'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        preexec_fn=os.setsid)
    sleep(10)
    print("[INFO]: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), " Appium server started.")


def stop_appium():
    """
    Kill node process
    """
    subprocess.call(('pkill', 'node'))
    print("[INFO]: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), " Appium server stopped.")
