########################

CameraStreamerClass_ReubenPython2and3Class

Code (including ability to hook to Tkinter GUI) that uses OpenCV to capture, JPEG-encode, and save an image-stream from a USB camera (like a webcam).

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision J, 12/30/2025

Verified working on: Python 3.12/13 for Windows 10/11 64-bit (Backend = "CAP_DSHOW") and Raspberry Pi Bullseye (Backend = "CAP_ANY").

Helper files (related to but not critical for core class functionality):

1. OpenCVwriteVideoFromImageSequence_ReubenPython2and3.py

2. OpenCVgetFOURCCfromVideoCapture_ReubenPython2and3.py

3. FFMPEG__ListDshowDevices_VideoAndAudio__ListOutputFormatsForVideoDevices_ReubenPython2and3.py

4. OpenCVsetEnableStateOfWarnings_ReubenPython2and3.py

########################  

########################### Python module installation instructions, all OS's

CameraStreamerClass_ReubenPython2and3Class, ListOfModuleDependencies: ['cv2', 'numpy', 'ReubenGithubCodeModulePaths']

CameraStreamerClass_ReubenPython2and3Class, ListOfModuleDependencies_TestProgram: ['keyboard', 'MyPrint_ReubenPython2and3Class', 'numpy', 'ReubenGithubCodeModulePaths']

CameraStreamerClass_ReubenPython2and3Class, ListOfModuleDependencies_NestedLayers: []

CameraStreamerClass_ReubenPython2and3Class, ListOfModuleDependencies_All:['cv2', 'keyboard', 'MyPrint_ReubenPython2and3Class', 'numpy', 'ReubenGithubCodeModulePaths']

To install the cv2 Python module using pip:

pip install opencv-contrib-python==4.12.0.88 #As of 12/30/25

###########################
