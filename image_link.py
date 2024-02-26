import numpy as np
import cv2
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.title("Image Colorization App")

def colorize_image(bw_image):

    prototxt_path = 'models/colorization_deploy_v2.prototxt'
    model_path = 'models/colorization_release_v2.caffemodel'
    kernel_path = 'models/pts_in_hull.npy'

    net = cv2.dnn.readNetFromCaffe(prototxt_path,model_path)
    points = np.load(kernel_path)
    points = points.transpose().reshape(2,313,1,1)

    net.getLayer(net.getLayerId("class8_ab")).blobs = [points.astype(np.float32)]
    net.getLayer(net.getLayerId("conv8_313_rh")).blobs = [np.full([1, 313], 2.606,dtype="float32")]

    normalized = bw_image.astype("float32")/255.0
    lab = cv2.cvtColor(normalized, cv2.COLOR_RGB2LAB)

    resized = cv2.resize(lab,(224,224))
    L = cv2.split(resized)[0]
    L -=50

    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0,:,:,:].transpose((1,2,0))
    ab=cv2.resize(ab,(bw_image.shape[1],bw_image.shape[0]))

    L=cv2.split(lab)[0]
    colorized =np.concatenate((L[:,:,np.newaxis],ab),axis=2)
    colorized = cv2.cvtColor(colorized,cv2.COLOR_LAB2RGB)
    colorized = (255.0*colorized).astype("uint8")
    return colorized


# Main Streamlit app
image_url = st.text_input("Enter the URL of a black and white image(Copy image address)")

if image_url:
    try:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        if st.button('Colorize'):
            colorized_image = colorize_image(np.array(image))
            if colorized_image is not None:
                st.image(colorized_image, caption='Colorized Image', use_column_width=True)
    except Exception as e:
        st.error(f"Error: {e}")
