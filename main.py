#import subprocess

# Define the package name you want to install
#package_name = "numpy"

# Use subprocess to run the pip install command
#subprocess.check_call(["pip", "install", package_name])

# Define the package name you want to install
#package_name = "opencv-python"
import captured as cp
import image_selector as ims
import numpy as np
import cv2

photo_folder_path = r'E:\open-cv\Photos'
latest_image_path = ims.get_latest_image(photo_folder_path)
img = cv2.imread(latest_image_path)
cv2.imshow('real_image',img)
# Use subprocess to run the pip install command
#subprocess.check_call(["pip", "install", package_name])


prototxt_path = 'models/colorization_deploy_v2.prototxt'
model_path = 'models/colorization_release_v2.caffemodel'
kernel_path = 'models/pts_in_hull.npy'

#bw_image=bs.img


#bw_image=gray_weighted
bw_image = img
cv2.imshow("BW Image",bw_image)

net = cv2.dnn.readNetFromCaffe(prototxt_path,model_path)
points = np.load(kernel_path)
points = points.transpose().reshape(2,313,1,1)

net.getLayer(net.getLayerId("class8_ab")).blobs = [points.astype(np.float32)]
net.getLayer(net.getLayerId("conv8_313_rh")).blobs = [np.full([1, 313], 2.606,dtype="float32")]


#bw_image = cv2.cvtColor(bw_image, cv2.COLOR_GRAY2BGR)


normalized = bw_image.astype("float32")/255.0

lab = cv2.cvtColor(normalized, cv2.COLOR_BGR2LAB)


resized = cv2.resize(lab,(224,224))
L = cv2.split(resized)[0]
L -=50

net.setInput(cv2.dnn.blobFromImage(L))
ab = net.forward()[0,:,:,:].transpose((1,2,0))
ab=cv2.resize(ab,(bw_image.shape[1],bw_image.shape[0]))

L=cv2.split(lab)[0]
colorized =np.concatenate((L[:,:,np.newaxis],ab),axis=2)
colorized = cv2.cvtColor(colorized,cv2.COLOR_LAB2BGR)
colorized = (255.0*colorized).astype("uint8")

cv2.imshow("Colorized",colorized)
cv2.waitKey(0)
cv2.destroyAllWindows()