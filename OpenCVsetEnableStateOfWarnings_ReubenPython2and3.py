# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision I, 02/02/2025

Verified working on: Python 3.8 for Windows 10 64-bit.
'''

__author__ = 'reuben.brewer'

#########################################################
import os
import sys
import traceback
#########################################################

##########################################################################################################
##########################################################################################################
def OpenCVsetEnableStateOfWarnings(EnabledState):

    try:
        EnabledState = int(EnabledState)

        if EnabledState in [0, 1]:

            #NOTE THAT THE WARNINGS WILL STAY SUPPRESSED PERMANENTLY BUT ONLY ON CMD TERMINALS OPENED AFTER THIS FUNCTION IS CALLED
            #(NOT IN CURRENT TERMINAL THAT CALLS THIS FUNCTION).

            os.system("SETX OPENCV_VIDEOIO_DEBUG {0}".format(str(EnabledState)))

            #os.environ["OPENCV_VIDEOIO_DEBUG"] = str(EnabledState) #Doesn't work!

            print("@@@@@@@@@@ OpenCVsetEnableStateOfWarnings fired for EnabledState = " + str(EnabledState) + " @@@@@@@@@@")

            '''
            set modifies the current shell's (the window's) environment values, and the change is available immediately, but it is temporary. 
            The change will not affect other shells that are running, and as soon as you close the shell, the new value is lost until such time as you run set again.

            setx modifies the value permanently, which affects all future shells, but does not modify the environment of the shells already running. 
            You have to exit the shell and reopen it before the change will be available, but the value will remain modified until you change it again. 
            setx OPENCV_VIDEOIO_DEBUG 0
            '''

        else:
            print("OpenCVsetEnableStateOfWarnings: Error, EnabledState must be 0 or 1.")

    except:
        exceptions = sys.exc_info()[0]
        print("OpenCVsetEnableStateOfWarnings, exceptions: %s" % exceptions)
        traceback.print_exc()

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    OpenCVsetEnableStateOfWarnings(0)

##########################################################################################################
##########################################################################################################