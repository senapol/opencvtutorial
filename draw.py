import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')  #creates a black image
cv.imshow('Blank', blank)

img = cv.imread('Resources/Photos/cat.jpg')  #returns image as matrix of pixels
cv.imshow('Cat', img)  #displays image

cv.waitKey(0)