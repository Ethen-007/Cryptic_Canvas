import streamlit as st
import numpy as np
import cv2

def colorize_image(img):
    prototxt_path = 'models/colorization_deploy_v2.prototxt'
    model_path = 'models/colorization_release_v2.caffemodel'
    kernel_path = 'models/pts_in_hull.npy'

    net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
    points = np.load(kernel_path)
    points = points.transpose().reshape(2, 313, 1, 1)

    net.getLayer(net.getLayerId("class8_ab")).blobs = [points.astype(np.float32)]
    net.getLayer(net.getLayerId("conv8_313_rh")).blobs = [np.full([1, 313], 2.606, dtype="float32")]

    normalized = img.astype("float32") / 255.0
    lab = cv2.cvtColor(normalized, cv2.COLOR_RGB2LAB)

    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50

    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab = cv2.resize(ab, (img.shape[1], img.shape[0]))

    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2RGB)
    colorized = (255.0 * colorized).astype("uint8")
    return colorized

def main():
    st.title("Image Colorization App")

    # OpenCV setup for camera capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Failed to open camera.")

    if st.button("Capture Image"):
        ret, frame = cap.read()
        if ret:
            st.image(frame, channels="BGR", caption="Captured Image")
            colorized_img = st.cache_data(colorize_image)(frame)
            st.image(colorized_img, caption="Colorized Image", channels="RGB")
        else:
            st.error("Failed to capture image from camera.")

    cap.release()

if __name__ == "__main__":
    main()

