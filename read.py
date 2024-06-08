import cv2 as cv

# img = cv.imread('Resources/Photos/cat.jpg')  #returns image as matrix of pixels

# cv.imshow('Cat', img)  #displays image


# cv.waitKey(0) #waits for key press to close window

# Reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4') #0 is the default camera

while True:
    isTrue, frame = capture.read() # reads video frame by frame
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #if 'd' key is pressed, break
        break

capture.release() #release video
cv.destroyAllWindows() #destroy windows
# -215 Assertion failed error means that the video ran out of frames
