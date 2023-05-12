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
import struct
import cv2
import traceback
###################################################

##########################################################################################################
##########################################################################################################
def OpenCVgetFOURCCfromVideoCapture(VideoCaptureObject):

    FOURCC_int = -1
    FOURCC_string = ""

    try:
        FOURCC_int = int(VideoCaptureObject.get(cv2.CAP_PROP_FOURCC))

        ################################################### BOTH OF THESE LINES WORK
        # FOURCC_string = "%s" % struct.pack("<I", FOURCC_int)
        FOURCC_string = "".join([chr((int(FOURCC_int) >> 8 * i) & 0xFF) for i in range(4)])
        ###################################################

    except:
        exceptions = sys.exc_info()[0]
        print("OpenCVgetFOURCCfromVideoCapture: Exceptions, %s" % exceptions)
        #traceback.print_exc()

    return [FOURCC_int, FOURCC_string]
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    ImageSequenceDirectory = os.getcwd()
    ImageName = "WIN_20220524_16_38_58_Pro.jpg"

    VideoCaptureObject = cv2.VideoCapture(ImageSequenceDirectory + "\\" + ImageName)

    [FOURCC_int, FOURCC_string] = OpenCVgetFOURCCfromVideoCapture(VideoCaptureObject)

    print("FOURCC_int:" + str(FOURCC_int))
    print("FOURCC_string:" + FOURCC_string)

##########################################################################################################
##########################################################################################################