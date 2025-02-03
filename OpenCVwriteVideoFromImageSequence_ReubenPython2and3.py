# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision I, 02/02/2025

Verified working on: Python 2.7, 3.8 for Windows 10 64-bit.
'''

__author__ = 'reuben.brewer'

###################################################
import os
import sys
import cv2
import numpy
import glob
import traceback
###################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    try:
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        '''
        In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
        In Windows: DIVX (More to be tested and added)
        '''
        #fourcc = -1 #-1 makes the compression dialog pop-up
        #fourcc = 0 #lossless
        #fourcc = cv2.VideoWriter_fourcc(*'LAGS') #MJPG works with Sony Vegas #fourcc = 1397178700 #int that corresponds to lossless "LAGS"
        #fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        #fourcc = cv2.VideoWriter_fourcc(*'YUYV')

        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # similar to H264
        #fourcc = cv2.VideoWriter_fourcc('a', 'v', 'c', '1') #similar to H264

        ImageSequenceDirectoryFullPath = "G:\\My Drive\\CodeReuben\\ArucoTagDetectionFromCameraFeed_ReubenPython3Class\\ArucoTagImages"

        ListOfFilterSubstrings = ["CAM0", "CAM1"]
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        list_of_files_all = glob.glob(ImageSequenceDirectoryFullPath + "\\*.jpg")  # * means all if need specific format then *.csv
        #print(list_of_files_all)

        list_of_lists_camera_sorted = []
        for FilterSubstring in ListOfFilterSubstrings:
            filtered_for_one_camera_TEMP = list(filter(lambda k: FilterSubstring in k, list_of_files_all))
            list_of_lists_camera_sorted.append(filtered_for_one_camera_TEMP)

        #print(list_of_lists_camera_sorted)
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        FPS_list = []
        for camera_number, list_of_camera_filenames in enumerate(list_of_lists_camera_sorted):
            number_of_frames = len(list_of_camera_filenames)
            #print("Camera " + str(camera_number) + " has " + str(number_of_frames) + " frames.")

            time_in_milliseconds_last = 0.0
            if number_of_frames > 1:
                #print("Processing frames from camera " + str(camera_number))

                frequency_list = []
                for frame_filename in list_of_camera_filenames[1:]:
                    image_filename = frame_filename
                    #print image_filename

                    start_index = image_filename.find("TIMEms") + len("TIMEms")
                    end_index = image_filename.find("_Frame")
                    time_in_milliseconds = float(image_filename[start_index:end_index])
                    #print(time_in_milliseconds)
                    deltaT = time_in_milliseconds - time_in_milliseconds_last
                    #print(deltaT)
                    if deltaT > 0.0:
                        frequency_list.append(1.0/deltaT)

                    time_in_milliseconds_last = time_in_milliseconds

                print(frequency_list)
                if len(frequency_list) >1:
                    FPS = int(round(1000.0*numpy.mean(frequency_list[1:])))
                else:
                    FPS = -1

                FPS_list.append(FPS)

                image = cv2.imread(image_filename)
                image_height, image_width = image.shape[:2]
                #print("Image is " + str(image_width) + " x " + str(image_height))

                VideoFilename = ImageSequenceDirectoryFullPath + "\\Video_" + str(camera_number) + ".avi"
                print("Video filename: " + VideoFilename)
                VideoWriter_object = cv2.VideoWriter(VideoFilename, fourcc, float(FPS), (image_width,image_height))

                for frame_number, frame_filename in enumerate(list_of_camera_filenames[1:]):
                    frame_image = cv2.imread(frame_filename)
                    VideoWriter_object.write(frame_image)
                    #print("Writing camera number " + str(camera_number) + ", frame number " + str(frame_number) + " of " + str(len(list_of_camera_filenames[1:])))
                VideoWriter_object.release()


        print("FPS_list: " + str(FPS_list))
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

    except:
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        exceptions = sys.exc_info()[0]
        print("Parsing ARGV_1, exceptions: %s" % exceptions)
        traceback.print_exc()
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
