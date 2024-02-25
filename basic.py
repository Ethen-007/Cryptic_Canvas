# import cv2 as cv
# import captured as cp
# import image_selector as ims
# import os
# import shutil

# photo_folder_path = r'E:\open-cv\Photos'
# latest_image_path = ims.get_latest_image(photo_folder_path)
# img = cv.imread(latest_image_path)
# cv.imshow('real_image',img)

# #converting to grayscle
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# #converting back to color
# # color=cv.cvtColor(gray,cv.COLOR_)
# # cv.imshow('color',color)

# #Blurring an image
# blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

# #edge cascade
# canny=cv.Canny(img,125,175)
# cv.imshow('Canny edges',canny)
# #adding far less edges
# #canny=cv.Canny(blur,125,175)
# #cv.imshow('canny-blur',canny)

# #dilating the image
# # dilated=cv.dilated(canny,(7,7),iterations=1)
# # cv.imshow('Dilated',dilated)
# # #Eroded
# # eroded=cv.erode(dilated,(3,3),iterations=1)
# # cv.imshow('Eroded',eroded)

# # #Resize
# # resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
# # cv.imshow('Resized',resized)

# #Cropping images
# cropped=img[50:200,200:400]#array slicing becoz images are arrays 
# cv.imshow('Cropped',cropped)

# cv.waitKey(0)
