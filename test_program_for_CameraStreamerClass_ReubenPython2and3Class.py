# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision G, 05/10/2023

Verified working on: Python 3.8 for Windows10 64-bit (no testing on Raspberry Pi or Mac testing yet).
'''

__author__ = 'reuben.brewer'

#########################################################
from CameraStreamerClass_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
#########################################################

#########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
import numpy
import argparse
#########################################################

#########################################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
#########################################################

#########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#########################################################

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def TestButtonResponse():
    global MyPrint_ReubenPython2and3ClassObject
    global USE_MYPRINT_FLAG

    if USE_MYPRINT_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.my_print("Test Button was Pressed!")
    else:
        print("Test Button was Pressed!")
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global CameraStreamerClass_ReubenPython2and3ClassObject
    global CameraStreamerClass_OPEN_FLAG
    global SHOW_IN_GUI_CameraStreamerClass_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG
    global SHOW_IN_GUI_MYPRINT_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if CameraStreamerClass_OPEN_FLAG == 1 and SHOW_IN_GUI_CameraStreamerClass_FLAG == 1:
                CameraStreamerClass_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MYPRINT_OPEN_FLAG == 1 and SHOW_IN_GUI_MYPRINT_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback():
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_CameraStreamerClass
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_CameraStreamerClass = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_CameraStreamerClass, text='   CAMERA   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############
        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_CameraStreamerClass = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    TestButton = Button(Tab_MainControls, text='Test Button', state="normal", width=20, command=lambda i=1: TestButtonResponse())
    TestButton.grid(row=0, column=0, padx=5, pady=1)
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_CameraStreamerClass_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    #################################################
    #################################################
    argparse_Object = argparse.ArgumentParser()
    #nargs='?', const='arg_was_not_given' is the key to allowing us to not input an argument (use Pycharm "run")
    argparse_Object.add_argument("-c", "--camera", nargs='?', const='arg_was_not_given', required=False, help="Camera number in the set [0, 1, ..., TotalNumberOfCameras]")
    ARGV_Dict = vars(argparse_Object.parse_args())
    print("ARGV_Dict: " + str(ARGV_Dict))

    if ARGV_Dict["camera"] != None:
        camera_selection_number = int(ARGV_Dict["camera"])
    else:
        camera_selection_number = 0

    print("camera_selection_number: " + str(camera_selection_number))
    #################################################
    #################################################

    #################################################
    #################################################
    global my_platform

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

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_CameraStreamerClass_FLAG
    USE_CameraStreamerClass_FLAG = 1

    global USE_MYPRINT_FLAG
    USE_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_CameraStreamerClass_FLAG
    SHOW_IN_GUI_CameraStreamerClass_FLAG = 1

    global SHOW_IN_GUI_MYPRINT_FLAG
    SHOW_IN_GUI_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_CameraStreamerClass
    global GUI_COLUMN_CameraStreamerClass
    global GUI_PADX_CameraStreamerClass
    global GUI_PADY_CameraStreamerClass
    global GUI_ROWSPAN_CameraStreamerClass
    global GUI_COLUMNSPAN_CameraStreamerClass
    GUI_ROW_CameraStreamerClass = 1

    GUI_COLUMN_CameraStreamerClass = 0
    GUI_PADX_CameraStreamerClass = 1
    GUI_PADY_CameraStreamerClass = 10
    GUI_ROWSPAN_CameraStreamerClass = 1
    GUI_COLUMNSPAN_CameraStreamerClass = 1

    global GUI_ROW_MYPRINT
    global GUI_COLUMN_MYPRINT
    global GUI_PADX_MYPRINT
    global GUI_PADY_MYPRINT
    global GUI_ROWSPAN_MYPRINT
    global GUI_COLUMNSPAN_MYPRINT
    GUI_ROW_MYPRINT = 2

    GUI_COLUMN_MYPRINT = 0
    GUI_PADX_MYPRINT = 1
    GUI_PADY_MYPRINT = 10
    GUI_ROWSPAN_MYPRINT = 1
    GUI_COLUMNSPAN_MYPRINT = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 70

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_CameraStreamerClass
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30
    #################################################
    #################################################

    #################################################
    #################################################

    #################################################
    #LET ARGV FIGURE THIS OUT camera_selection_number = 0 #The camera number will be an integer in set [0, 1...NumberOfUSBcameraPluggedIn]
    camera_frame_rate = 30
    image_width = 640#640#1280#1920
    image_height = 480#480#720#1080
    image_jpg_encoding_quality = 25
    CameraSetting_Autofocus = 0
    CameraSetting_Autoexposure = 1
    CameraSetting_exposure = -7
    CameraSetting_gain = 100
    CameraSetting_brightness = 75
    CameraSetting_contrast = 32
    CameraSetting_saturation = 60
    CameraSetting_hue = 0
    DrawCircleAtImageCenterFlag = 0
    EnableCameraEncodeThreadFlag = 1
    EnableImageSavingThreadFlag = 1
    RemoveFisheyeDistortionFromImage_Flag = 0
    CameraCalibrationParametersDict = dict([("fx", 532.972485),
                                                ("fy", 532.972485),
                                                ("cx", 320.000000),
                                                ("cy", 240.000000),
                                                ("k1", -1.105115),
                                                ("k2", 1.372161),
                                                ("p1", -0.001400),
                                                ("p2", -0.021523)])
    TkinterPreviewImageScalingFactor = 1.0
    #################################################

    #################################################
    global CameraStreamerClass_ReubenPython2and3ClassObject

    global CameraStreamerClass_OPEN_FLAG
    CameraStreamerClass_OPEN_FLAG = -1

    global CameraStreamerClass_MostRecentDict
    CameraStreamerClass_MostRecentDict = dict()

    global CameraStreamerClass_MostRecentDict_OriginalImage
    CameraStreamerClass_MostRecentDict_OriginalImage = numpy.zeros((image_height, image_width, 3), numpy.uint8)

    global CameraStreamerClass_MostRecentDict_Time
    CameraStreamerClass_MostRecentDict_Time = -11111.0
    #################################################

    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MYPRINT_OPEN_FLAG
    MYPRINT_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
        Tab_MainControls = None
        Tab_CameraStreamerClass = None
        Tab_MyPrint = None
    #################################################
    #################################################

    #################################################
    #################################################
    global CameraStreamerClass_ReubenPython2and3ClassObject_GUIparametersDict
    CameraStreamerClass_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_CameraStreamerClass_FLAG),
                                    ("root", Tab_CameraStreamerClass),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_CameraStreamerClass),
                                    ("GUI_COLUMN", GUI_COLUMN_CameraStreamerClass),
                                    ("GUI_PADX", GUI_PADX_CameraStreamerClass),
                                    ("GUI_PADY", GUI_PADY_CameraStreamerClass),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_CameraStreamerClass),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_CameraStreamerClass)])

    global CameraStreamerClass_ReubenPython2and3ClassObject_setup_dict
    CameraStreamerClass_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", CameraStreamerClass_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                        ("CameraCaptureThread_TimeToSleepEachLoop", 0.001),
                                                                        ("CameraEncodeThread_TimeToSleepEachLoop", 0.001),
                                                                        ("ImageSavingThread_TimeToSleepEachLoop", 0.001),
                                                                        ("NameToDisplay_UserSet", "Reuben Camera Test"),
                                                                        ("TkinterPreviewImageScalingFactor", TkinterPreviewImageScalingFactor), #percent size of the image that will be displayed within Tkinter.
                                                                        ("camera_selection_number", camera_selection_number),
                                                                        ("camera_frame_rate", camera_frame_rate),
                                                                        ("image_width", image_width),
                                                                        ("image_height", image_height),
                                                                        ("image_jpg_encoding_quality", image_jpg_encoding_quality),
                                                                        ("CameraSetting_Autofocus", CameraSetting_Autofocus),
                                                                        ("CameraSetting_Autoexposure", CameraSetting_Autoexposure),
                                                                        ("CameraSetting_exposure", CameraSetting_exposure),
                                                                        ("CameraSetting_gain", CameraSetting_gain),
                                                                        ("CameraSetting_brightness", CameraSetting_brightness),
                                                                        ("CameraSetting_contrast", CameraSetting_contrast),
                                                                        ("CameraSetting_saturation", CameraSetting_saturation),
                                                                        ("CameraSetting_hue", CameraSetting_hue),
                                                                        ("DrawCircleAtImageCenterFlag", DrawCircleAtImageCenterFlag),
                                                                        ("EnableCameraEncodeThreadFlag", EnableCameraEncodeThreadFlag),
                                                                        ("EnableImageSavingThreadFlag", EnableImageSavingThreadFlag),
                                                                        ("OpenCVbackendToUseEnglishName","CAP_MSMF"),#CAP_MSMF CAP_DSHOW CAP_ANY
                                                                        ("RemoveFisheyeDistortionFromImage_Flag", RemoveFisheyeDistortionFromImage_Flag),
                                                                        ("CameraCalibrationParametersDict", CameraCalibrationParametersDict)])

    if USE_CameraStreamerClass_FLAG == 1:
        try:
            CameraStreamerClass_ReubenPython2and3ClassObject = CameraStreamerClass_ReubenPython2and3Class(CameraStreamerClass_ReubenPython2and3ClassObject_setup_dict)
            CameraStreamerClass_OPEN_FLAG = CameraStreamerClass_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("CameraStreamerClass_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MYPRINT_FLAG),
                                                                        ("root", Tab_MyPrint),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MYPRINT),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MYPRINT),
                                                                        ("GUI_PADX", GUI_PADX_MYPRINT),
                                                                        ("GUI_PADY", GUI_PADY_MYPRINT),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MYPRINT),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MYPRINT)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            MYPRINT_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_CameraStreamerClass_FLAG == 1 and CameraStreamerClass_OPEN_FLAG != 1:
        print("Failed to open CameraStreamerClass_ReubenPython2and3Class.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1 and MYPRINT_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    print("Starting main loop 'test_program_for_CameraStreamerClass_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################

        ################################################### GET's
        if CameraStreamerClass_OPEN_FLAG == 1:

            CameraStreamerClass_MostRecentDict = CameraStreamerClass_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "Time" in CameraStreamerClass_MostRecentDict:
                CameraStreamerClass_MostRecentDict_OriginalImage = CameraStreamerClass_MostRecentDict["OriginalImage"]
                CameraStreamerClass_MostRecentDict_Time = CameraStreamerClass_MostRecentDict["Time"]

                #print("CameraStreamerClass_MostRecentDict_Time: " + str(CameraStreamerClass_MostRecentDict_Time))
        ###################################################

        time.sleep(0.030)
    #################################################
    #################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_CameraStreamerClass_ReubenPython2and3Class.")

    #################################################
    if CameraStreamerClass_OPEN_FLAG == 1:
        CameraStreamerClass_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if MYPRINT_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################