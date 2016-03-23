r""" Requirements:
Before start working with ios_commands framework,
you need to install libimobiledevice library.
For more details look at:
 - http://www.libimobiledevice.org/
 - https://github.com/benvium/libimobiledevice-macosx source code and installation guide
"""
import os
import subprocess
import signal


def take_scrennshot(file_name):
    cmd = 'idevicescreenshot'
    output = subprocess.getstatusoutput(cmd)
    if output[0]:
        raise AssertionError('Non zero status output. \n %s' % output[1])
    print('INFO: ','adb command output:', output[1])
    return output[1]





def _execute_command(cmd, *args):
    """
    Internal function execute adb commands in terminal
    :param cmd: adb command
    :param args: options
    """
    cmd = ''.join(cmd) + ' '.join(args)
    output = subprocess.getstatusoutput(cmd)
    print('INFO: adb command: "%s %s " executed' % (cmd, str(args)))
    if output[0]:
        raise AssertionError('Non zero status output. \n %s' % output[1])
    print('INFO: ','adb command output:', output[1])
    return output[1]


def _execute_subprocess(cmd):
    """
    Internal function execute command in subprocess
    :param cmd: command
    """
    subprocess.Popen(cmd,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    shell=True, preexec_fn=os.setsid)


def _kill_subprocess():
    """
    kills executeted subprocess by KeyboardInterupt
    """
    pid = os.getpid()
    try:
        os.kill(pid, signal.SIGINT)
    except (KeyboardInterrupt, SystemExit):
        print('INFO: Subprocess killed')



