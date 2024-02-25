import cv2 as cv
import numpy as np
img=cv.imread('Photos/girl.jpg')
cv.imshow('Girls',img)

blank=np.zeros(img.shape[:2],dtype='uint8')


b,g,r=cv.split(img)
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('red',r)

merged=cv.merge([b,g,r])
cv.imshow('Merged IMage',merged)

print(img.shape)
print(b.shape)
print(g.shape)

cv.waitKey(0)
