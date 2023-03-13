# Video_Conversion_with_GUI

This is a Python code that converts a video file into a new format using OpenCV library. It includes a graphical user interface (GUI) to allow the user to select the input video file and choose the codec to use for the output video.

# Getting Started

1. Clone this repository or download the code files.
2. Install the required Python libraries: OpenCV, tkinter.
3. Run the Python script video_conversion_gui.py.

# How to Use

Click the 'Select Video' button to open a file dialog window and choose the input video file.
Enter the FourCC codec to use for the output video in the 'Codec Selection' dialog window.
Click the 'Convert Video' button to start the conversion process.
The converted video will be saved in the same directory as the input video file with the specified FourCC codec and '.avi' file extension.

# Notes

FourCC is a four-byte code used to specify the video codec. You can find a list of FourCC codes here.
This code only supports the input video files that OpenCV can read. You can find the list of supported formats here.
