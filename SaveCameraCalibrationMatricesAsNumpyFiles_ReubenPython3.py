# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision J, 12/30/2025

Verified working on: Python 3.12/13 for Windows 10/11 64-bit (Backend = "CAP_DSHOW") and Raspberry Pi Bullseye (Backend = "CAP_ANY").
'''

__author__ = 'reuben.brewer'

#########################################################
import numpy
#########################################################

####
rms = 0.201598
fx = 608.186873
fy = 608.186873
cx = 320.000000
cy = 240.000000
k1 = -0.460387
k2 = 0.276330
p1 = 0.003287
p2 = 0.008647

hfov = 57.6#deg
vfov = 44.8#deg
####

####
Kmatrix_CameraIntrinsicsMatrix = numpy.zeros((3, 3), dtype=float)
Kmatrix_CameraIntrinsicsMatrix[0, 0] = float(fx)
Kmatrix_CameraIntrinsicsMatrix[1, 1] = float(fy)
Kmatrix_CameraIntrinsicsMatrix[2, 2] = 1.0
Kmatrix_CameraIntrinsicsMatrix[0, 2] = float(cx)
Kmatrix_CameraIntrinsicsMatrix[1, 2] = float(cy)
####

####
Darray_DistortionCoefficients = numpy.zeros((1, 4), dtype=float)
Darray_DistortionCoefficients[0, 0] = float(k1)
Darray_DistortionCoefficients[0, 1] = float(k2)
Darray_DistortionCoefficients[0, 2] = float(p1)
Darray_DistortionCoefficients[0, 3] = float(p2)
####

####
numpy.save("Kmatrix_CameraIntrinsicsMatrix.npy", Kmatrix_CameraIntrinsicsMatrix, allow_pickle=True)
numpy.save("Darray_DistortionCoefficients.npy", Darray_DistortionCoefficients, allow_pickle=True)
####