
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


## Part 2 : Capturing and Preprocessing Data (Day 2) ##

## Initialize variables and lists
faces_data = []
i = 0

## Prompt the user to input their name
name = input("Enter Your Name: ")

## Continuously capture and process video frames
while True:
    ret,frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    ## Process and collect face data
    for (x, y, w, h) in faces:
         crop_img=frame[y:y+h, x:x+w, :]
         resized_img=cv2.resize(crop_img, (50,50))
         if len(faces_data)<=100 and i%10==0:
            faces_data.append(resized_img)
         i=i+1
    
    ## Display the frame with face count
         cv2.putText(frame, str(len(faces_data)), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 1)
         cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    ## Break the loop when needed
    if k==ord('q') or len(faces_data) == 100:
       break
video.release()
cv2.destroyAllWindows()

## Code Explanation:
# - Initialize an empty list to store captured face data.
# - Prompt the user to input their name.
# - Continuously capture video frames from the webcam.
# - Convert each frame to grayscale for face detection.
# - Detect faces in the grayscale frame using the Haar Cascade classifier.
# - Crop and resize detected faces to 50x50 pixels.
# - Collect face data, appending it to the 'faces_data' list.
# - Display the number of captured faces on the frame.

## Why Used:
# - Capturing and preprocessing data is essential for building a dataset.
# - Grayscale conversion simplifies face detection.
# - Resizing ensures consistent data dimensions.
# - Counting and displaying the number of faces aids user feedback.

