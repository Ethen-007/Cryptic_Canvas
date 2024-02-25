import cv2
import os
import shutil
from datetime import datetime

def capture_and_save_photo(folder_path):
    # Capture a photo using the default camera (usually camera index 0)
    capture = cv2.VideoCapture(0)
    
    # Read a single frame from the camera
    ret, frame = capture.read()

    # Release the capture object
    capture.release()

    if ret:
        # Generate a unique filename based on the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"photo_{timestamp}.jpg"

        # Save the captured photo to the specified folder
        photo_path = os.path.join(folder_path, filename)
        cv2.imwrite(photo_path, frame)

        print(f"Photo captured and saved to {photo_path}")
    else:
        print("Failed to capture a photo.")

def move_photo_to_folder(source_path, destination_folder):
    # Make sure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Move the photo to the designated folder
    shutil.move(source_path, destination_folder)

    print(f"Photo moved to {destination_folder}")

# Example usage with the new folder path:
folder_path = "E:\open-cv\Photos"
capture_and_save_photo(folder_path)

# Move the photo to another folder if needed
# destination_folder = "path/to/another/folder"
# move_photo_to_folder(os.path.join(folder_path, "your_photo.jpg"), destination_folder)
