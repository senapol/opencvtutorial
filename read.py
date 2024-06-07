import cv2 as cv

img = cv.imread('Photos/cat.jpg')  #returns image as matrix of pixels

cv.imshow('Cat', img)  #displays image

cv.waitKey(0) #waits for key press to close window