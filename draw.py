import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')  #creates a black image
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[200:300,300:400] = 0,0,255
cv.imshow('Green', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,300), (0,255,0), thickness=2)
# or cv.filled/-1 for filled

cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (250,250), 40, (250,0,0), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (50,50), (200,200), (255,255,255), thickness=3)
cv.imshow('Line', blank)

cv.waitKey(0)