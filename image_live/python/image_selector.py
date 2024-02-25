import os

def get_latest_image(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter out non-image files if needed (e.g., only consider files with a certain extension)
    image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Check if there are any image files in the folder
    if not image_files:
        print("No image files found in the folder.")
        return None

    # Extract timestamps from filenames and find the latest one
    latest_image = max(image_files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

    # Return the full path to the latest image
    return os.path.join(folder_path, latest_image)
