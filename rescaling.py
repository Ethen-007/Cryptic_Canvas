import cv2 as cv
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.75):
    # Works on image,video and live-video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions= (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
cv.waitKey(0)
#Showing the resized image
resized_Image=rescaleFrame(img)
cv.imshow('image',resized_Image)

def changedRes(width,height):
    # Works only on live-video
    capture.set(3,width)#This function works only for live-video
    capture.set(4,height)

#Showing the resized video
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('video_resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.realease()
cv.destroyAllWindows()
