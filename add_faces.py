
## Part 1: Setting Up the Basics (Day 1) ##

# Libraries Used:
import cv2  ## OpenCV for computer vision
import numpy as np  ## NumPy for numerical operations
import os  ## OS module for file operations

## Initialize video capture from the default camera
video = cv2.VideoCapture(0)

## Load a Haar Cascade classifier for face detection
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

## Code Explanation:
# - Import necessary libraries for the project.
# - Initialize video capture from the default camera (camera index 0).
# - Load a Haar Cascade classifier for face detection from a data file.

## Needs:
# - Ensure 'haarcascade_frontalface_default.xml' exists in the 'data/' directory.
# - Have a webcam connected and accessible.

## Why Used:
# - cv2.VideoCapture is used to capture video frames from the webcam.
# - Haar Cascade classifier helps detect faces in the video frames.
# - NumPy is used for efficient array operations.
