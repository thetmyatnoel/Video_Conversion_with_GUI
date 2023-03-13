import cv2 as cv
import tkinter as tk
from tkinter import filedialog
import tkinter.simpledialog as simpledialog

# Function to get the input video file path using GUI
def get_video_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

# Function to get the codec to use for the output video using GUI
def get_codec():
    root = tk.Tk()
    root.withdraw()
    codec = simpledialog.askstring("Codec Selection", "Enter the FourCC codec to use:")
    return codec

# Get the input video file path and target format from GUI
video_file = get_video_file()
target_format = 'avi'

# Get the FourCC codec to use from GUI
target_fourcc = get_codec()

# Read the given video file
video = cv.VideoCapture(video_file)

if video.isOpened():
    target = cv.VideoWriter()
    while True:
        # Get an image from 'video'
        valid, img = video.read()
        if not valid:
            break

        if not target.isOpened():
            # Open the target video file
            target_file = video_file[:video_file.rfind('.')] + '.' + target_format
            fps = video.get(cv.CAP_PROP_FPS)
            h, w, *_ = img.shape
            is_color = (img.ndim > 2) and (img.shape[2] > 1)
            target.open(target_file, cv.VideoWriter_fourcc(*target_fourcc), fps, (w, h), is_color)

        # Add the image to 'target'
        target.write(img)

    target.release()
