import numpy as np
import cv2
import streamlit as st
import tempfile
import os

def rescaleFrame(frame, scale=0.55):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def color(frame):
    bw_image = frame
    normalized = bw_image.astype("float32") / 255.0
    lab = cv2.cvtColor(normalized, cv2.COLOR_BGR2LAB)

    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50

    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab = cv2.resize(ab, (bw_image.shape[1], bw_image.shape[0]))

    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = (255.0 * colorized).astype("uint8")
    return colorized

prototxt_path = 'models/colorization_deploy_v2.prototxt'
model_path = 'models/colorization_release_v2.caffemodel'
kernel_path = 'models/pts_in_hull.npy'

net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
points = np.load(kernel_path)
points = points.transpose().reshape(2, 313, 1, 1)

net.getLayer(net.getLayerId("class8_ab")).blobs = [points.astype(np.float32)]
net.getLayer(net.getLayerId("conv8_313_rh")).blobs = [np.full([1, 313], 2.606, dtype="float32")]

st.title("Video Colorization App")

uploaded_file = st.file_uploader("Choose a video file", type=['mp4'])

if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    capture = cv2.VideoCapture(tmp_file_path)
    colorized_placeholder = st.empty()
    bw_placeholder = st.empty()

    while True:
        isTrue, frame = capture.read()
        if not isTrue:
            break
        frame_resized = rescaleFrame(frame)
        colorized_frame = color(frame_resized)

        # Display the colorized frame
        colorized_placeholder.image(colorized_frame, channels="BGR", use_column_width=True)

        # Display the original frame (black and white)
        bw_placeholder.image(frame_resized, channels="BGR", use_column_width=True)

    # Close the video file and remove the temporary file
    capture.release()
    cv2.destroyAllWindows()
    cv2.waitKey(0)
    st.write("Video processing completed.")

    # Remove the temporary file
    if tmp_file_path:
        os.unlink(tmp_file_path)
