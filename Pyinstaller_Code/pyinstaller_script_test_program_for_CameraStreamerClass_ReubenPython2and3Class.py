'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision H, 09/22/2023

Verified working on: Python 3.8 for Windows10 64-bit (no testing on Raspberry Pi or Mac testing yet).
'''

#Before issuing, command "pip uninstall pathlib" to prevent getting the error "The 'pathlib' package is an obsolete backport of a standard library package and is incompatible with PyInstaller."
import os
import sys
import time
import platform
import subprocess
import traceback

if platform.system() == "Windows":

    VersionTextFileFullFilepath = os.getcwd() + "\\test_program_for_CameraStreamerClass_ReubenPython2and3Class_EXE_version.txt"
    IconFileFullFilepath = os.getcwd() + "\\CameraIcon.ico"
    PythonFileFullFilepath = os.getcwd() + "\\test_program_for_CameraStreamerClass_ReubenPython2and3Class.py"
    TestFileFullFilepath = os.getcwd() + "\\test.txt"


    #shell_command_to_issue = "pyinstaller " + os.getcwd() + "\\pyinstall_script_parameters_test_program_for_CameraStreamerClass_ReubenPython2and3Class.spec"

    shell_command_to_issue = "pyinstaller --onefile --console " +\
                            "--version-file " + VersionTextFileFullFilepath + \
                            " --icon " + IconFileFullFilepath + \
                             " " + PythonFileFullFilepath

    shell_command_to_issue = "start notepad \"" + TestFileFullFilepath + "\"" #I THINK THAT WE HAVE TO ISSUE FROM AN ADMINISTRATOR CONSOLE!!!

    print("shell_command_to_issue:" + shell_command_to_issue)

    ##########################################################################################################
    try:
        process = subprocess.Popen([shell_command_to_issue]) #subprocess.Popen doesn't wait for process to terminate
        time.sleep(2.0)
    except:
        exceptions = sys.exc_info()[0]
        print("Exceptions: %s" % exceptions)
        traceback.print_exc()
    ##########################################################################################################



#pyinstaller --onefile/onedir --console auto_calibration.py #Only use this line if you don't already have the spec file.

#Issue from an administrator cmd console:
#pyinstaller --onefile --console --version-file test_program_for_CameraStreamerClass_ReubenPython2and3Class_EXE_version.txt --icon CameraIcon.ico test_program_for_CameraStreamerClass_ReubenPython2and3Class.py