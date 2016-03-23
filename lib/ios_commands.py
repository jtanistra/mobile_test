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
from lib.logger import Logger
import shutil

class Commands(Logger):

    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/logs/'
        self.current_path = os.path.dirname(__file__)

    def take_scrennshot(self, file_name):
        cmd = 'idevicescreenshot ' + self.path + file_name
        self._execute_command(cmd)

    def _execute_command(self, cmd, *args):
        """
        Internal function execute adb commands in terminal
        :param cmd: adb command
        :param args: options
        """
        output = subprocess.getstatusoutput(cmd)
        self.logger('INFO', 'io commands executed "%s " executed' % cmd)
        if output[0]:
            raise AssertionError('Non zero status output. \n %s' % output[1])
        self.logger('INFO', 'ios commands output: %s' % output[1])
        print(os.path.dirname(__file__))
        return output[1]

# def _execute_subprocess(cmd):
#     """
#     Internal function execute command in subprocess
#     :param cmd: command
#     """
#     subprocess.Popen(cmd,
#                     stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                     shell=True, preexec_fn=os.setsid)
#
#
# def _kill_subprocess():
#     """
#     kills executeted subprocess by KeyboardInterupt
#     """
#     pid = os.getpid()
#     try:
#         os.kill(pid, signal.SIGINT)
#     except (KeyboardInterrupt, SystemExit):
#         print('INFO: Subprocess killed')
#
#
#
# if __name__=='__main__':
#     cmd = Commands()
#     cmd.take_scrennshot(file_name='asd.png')