import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')#uint8 is the datatype of an image
#(500,500,3)specifies the height,width and the color channels
cv.imshow('Blank',blank)

#1.Painting the image a color

# blank[:]=0,255,0#painting the blank green
# blank[200:300,300:400]=0,0,255
#painting a specific region

#Painting a rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1)
# #to paint the selected portion of blank entirely with green 
# # cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=cv.FILLED || thickess=-1)
# cv.imshow('Rectangle',blank)

#Drawing a circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[1]//2),40,(0,255,0),thickness=3)
# cv.imshow('Circle',blank)

#Drawing a line
# cv.line(blank,(100,250),(150,300),(255,255,255),thickness=3)
# cv.imshow('Line',blank)

#Writing a text
cv.putText(blank,'Hello',(0,255),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(255,0,255),2)
cv.imshow('Text',blank)
cv.waitKey(0)



# img=cv.imread('Photos/girl.img')
# cv.imshow('Girl',img)