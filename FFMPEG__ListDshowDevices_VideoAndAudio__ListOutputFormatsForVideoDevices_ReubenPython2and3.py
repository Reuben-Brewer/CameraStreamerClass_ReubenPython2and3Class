# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision G, 05/10/2023

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

###################################################
import os
import sys
import subprocess
import platform
import pexpect
import time
import datetime
import traceback
###################################################

##########################################################################################################
##########################################################################################################
def GetMyPlatformOS():

    my_platform = ""

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    return my_platform
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def IsInputList(InputToCheck):

    result = isinstance(InputToCheck, list)
    return result
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
def ListDshowDevices_VideoAndAudio(FFMPEGexeFullPath):

    DshowDeviceList = []

    try:
        my_platform = GetMyPlatformOS()

        ##########################################################################################################
        ##########################################################################################################
        if my_platform == "windows":

            shell_command_to_issue = "\"" + FFMPEGexeFullPath + "\\ffmpeg.exe\" -list_devices true -f dshow -i dummy"
            print("shell_command_to_issue: " + shell_command_to_issue)

            ##########################################################################################################
            '''
            https://stackoverflow.com/questions/70064040/ffmpeg-unexpected-exit-code-1-for-list-devices-and-list-options
            Will see "dummy: Immediate exit requested" in exception, and we won't get a return from the subprocess.check_output.
            This is why we have to get the data from the exception.
            We could change the FFMPEG source code to exit cleanly, but then we'd have to recompile
            '''

            try:
                WontReceiveThisReturnDueToException = subprocess.check_output(shell_command_to_issue, shell=True, stderr=subprocess.STDOUT)
            except Exception as e: #THIS "Exception as e" format is compatible in both Python2.7 and 3 and SAVES THE CONTENTS OF THE EXCEPTION
                shell_response_str = str(e.output)
            ##########################################################################################################

            ##########################################################################################################
            if sys.version_info[0] < 3:
                shell_response_ListOfStr = shell_response_str.split("\r\n")
            else:
                shell_response_ListOfStr = shell_response_str.split("\\r\\n")#PYTHON 3 DIFFERS IN HOW IT SPLITS BASED ON \r\n

            #print("\n $$$$ shell_response_ListOfStr: " + str(shell_response_ListOfStr) + "$$$$")
            ##########################################################################################################

            ##########################################################################################################
            for line_str in shell_response_ListOfStr:
                #print("\n$$$$ line_str:" + line_str + "$$$$")

                if line_str.lower().find("alternative") == -1 and line_str.lower().find("dshow") != -1 and line_str.lower().find("directshow") == -1:
                    line_ListOfStr = line_str.split("\"")

                    for Substring in line_ListOfStr:
                        Substring = Substring.strip()
                        if Substring != "" and Substring.lower().find("dshow") == -1:
                            DshowDeviceList.append(Substring)

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        else:
            print("ListCameras: Error, this code runs only on Windows!")
        ##########################################################################################################
        ##########################################################################################################

    except:
        exceptions = sys.exc_info()[0]
        print("ListDshowDevices_VideoAndAudio: Exceptions, %s" % exceptions)
        traceback.print_exc()

    return DshowDeviceList
##########################################################################################################
##########################################################################################################
##########################################################################################################

#######################################################################################################################
#######################################################################################################################
def ListOutputFormatsForVideoDevices(VideoDeviceName):

    if IsInputList(VideoDeviceName) == 1:
        print("ListOutputFormatsForVideoDevices: ERROR, must input the string name of a video device, not a list.")

    CodecList = []

    try:

        my_platform = GetMyPlatformOS()

        ##########################################################################################################
        ##########################################################################################################
        if my_platform == "windows":

            shell_command_to_issue = "\"" + FFMPEGexeFullPath + "\\ffmpeg.exe\" -f dshow -list_options true -i video=\"" + VideoDeviceName + "\""
            print("shell_command_to_issue: " + shell_command_to_issue)

            ##########################################################################################################
            '''
            https://stackoverflow.com/questions/70064040/ffmpeg-unexpected-exit-code-1-for-list-devices-and-list-options
            Will see "dummy: Immediate exit requested" in exception, and we won't get a return from the subprocess.check_output.
            This is why we have to get the data from the exception.
            We could change the FFMPEG source code to exit cleanly, but then we'd have to recompile
            '''

            try:
                WontReceiveThisReturnDueToException = subprocess.check_output(shell_command_to_issue, shell=True, stderr=subprocess.STDOUT)
            except Exception as e: #THIS "Exception as e" format is compatible in both Python2.7 and 3 and SAVES THE CONTENTS OF THE EXCEPTION
                shell_response_str = str(e.output)
            ##########################################################################################################

            ##########################################################################################################
            if sys.version_info[0] < 3:
                shell_response_ListOfStr = shell_response_str.split("\r\n")
            else:
                shell_response_ListOfStr = shell_response_str.split("\\r\\n")#PYTHON 3 DIFFERS IN HOW IT SPLITS BASED ON \r\n

            #print("\n $$$$ shell_response_ListOfStr: " + str(shell_response_ListOfStr) + "$$$$")
            ##########################################################################################################

            ##########################################################################################################
            codec_counter = 0
            pixel_format_EnglishName = ""
            for line_str in shell_response_ListOfStr:
                line_str = line_str.strip()

                if line_str.lower().find("dshow") != -1 and line_str.lower().find("directshow") == -1:
                    CodecList.append(line_str)
            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        else:
            print("ListOutputFormatsForVideoDevices: Error, this code runs only on Windows!")
        ##########################################################################################################
        ##########################################################################################################


    except:
        exceptions = sys.exc_info()[0]
        print("ListOutputFormatsForVideoDevices: Exceptions, %s" % exceptions)
        traceback.print_exc()

    return CodecList
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
if __name__ == '__main__':

    FFMPEGexeFullPath = "G:\My Drive\CodeReuben\FFMPEG_windows"

    DshowDeviceList = ListDshowDevices_VideoAndAudio(FFMPEGexeFullPath)
    print("DshowDeviceList: " + str(DshowDeviceList))

    #CodecList = ListOutputFormatsForVideoDevices("Integrated Camera")
    #CodecList = ListOutputFormatsForVideoDevices("HD USB Camera")
    #print("CodecList: " + str(CodecList))

 #######################################################################################################################
#######################################################################################################################