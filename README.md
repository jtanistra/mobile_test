# mobile_test

Project for testing s-labs mobile applications.

Available platforms: iOS and Android.

Requires environment:
 * appium - http://appium.io/
 * python >= 3.5
 * java - https://www.java.com/
 iOS:

    ** MacOS X 10.7
    ** Xcode
    ** mobiledevice - https://github.com/imkira/mobiledevice - brew install mobiledevice
    ** libimobiledevice - https://github.com/benvium/libimobiledevice-macosx
 
 Android
 
    ** Mac OSX 10.7+ or Windows 7+ or Linux
    ** Android SDK https://developer.android.com/sdk/installing/index.html

Requires python libraries:

 * appium-python-client - requrements.txt
 * selenium web driver = http://docs.seleniumhq.org - requirements.txt
 * behave - https://jenisys.github.io/behave.example/index.html# - requirements.txt

To install require python libraries type in terminal:

 * for python 3.5:
    ** pip3 install -r requirements.txt

To run your tests open directory with test package and type 'behave'

