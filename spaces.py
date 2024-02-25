import cv2 as cv
img=cv.imread('Photos/girl.jpg')
cv.imshow('Girl',img)

#BGR to Grayscle
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


# #BGR to HSV
# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('HSV',hsv)

# #BGR TO  L+A+B
# lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow('Lab',lab)

#Grayscale to BGR
# bgr=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
# cv.imshow('bgr',bgr)

# #bgr to hsv
# hsv=cv.cvtColor(bgr,cv.COLOR_BGR2HSV)
# cv.imshow('hsv',hsv)
cv.waitKey(0)