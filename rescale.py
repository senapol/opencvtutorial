import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')  #returns image as matrix of pixels

cv.imshow('Cat', img)  #displays image

def rescaleFrame(frame, scale=0.75):
    # Images, Videos, Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_img = rescaleFrame(img)
cv.imshow('Image', resized_img)

def changeRest(width, height):
    # Live video
    capture.set(3,width)
    capture.set(4,height)
    

# Reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4') #0 is the default camera

while True:
    isTrue, frame = capture.read() # reads video frame by frame

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): #if 'd' key is pressed, break
        break

capture.release() #release video
cv.destroyAllWindows() #destroy windows
# -215 Assertion failed error means that the video ran out of frames
