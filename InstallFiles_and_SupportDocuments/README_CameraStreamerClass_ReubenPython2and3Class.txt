########################

CameraStreamerClass_ReubenPython2and3Class

Code (including ability to hook to Tkinter GUI) that uses OpenCV to capture, JPEG-encode, and save an image-stream from a USB camera (like a webcam).

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision I, 02/02/2025

Verified working on:
Python 3.12 for Windows 11 64-bit and Raspberry Pi Bullseye (Backend = "CAP_ANY", Camera = ELP USB).

Helper files (related to but not critical for core class functionality):

1. OpenCVwriteVideoFromImageSequence_ReubenPython2and3.py

2. OpenCVgetFOURCCfromVideoCapture_ReubenPython2and3.py

3. FFMPEG__ListDshowDevices_VideoAndAudio__ListOutputFormatsForVideoDevices_ReubenPython2and3.py

4. OpenCVsetEnableStateOfWarnings_ReubenPython2and3.py

########################  

########################### Python module installation instructions, all OS's

CameraStreamerClass_ReubenPython2and3Class, ListOfModuleDependencies: ['cv2', 'future.builtins', 'numpy']

CameraStreamerClass_ReubenPython2and3Class, ListOfModuleDependencies_TestProgram: ['MyPrint_ReubenPython2and3Class', 'numpy']

CameraStreamerClass_ReubenPython2and3Class, ListOfModuleDependencies_NestedLayers: ['future.builtins']

CameraStreamerClass_ReubenPython2and3Class, ListOfModuleDependencies_All:['cv2', 'future.builtins', 'MyPrint_ReubenPython2and3Class', 'numpy']

To install the cv2 Python module using pip:

pip install opencv-contrib-python==4.5.5.64

###########################