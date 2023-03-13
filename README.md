# Video_Conversion_with_GUI

This is a Python code that converts a video file into a new format using OpenCV library. It includes a graphical user interface (GUI) to allow the user to select the input video file and choose the codec to use for the output video.

# Getting Started

1. Clone this repository or download the code files.
2. Install the required Python libraries: OpenCV, tkinter.
3. Run the Python script "video_converter_with_GUI.py".

# How to Use

1. Run the python script to open a file dialog window and choose the input video file.
2. Enter the FourCC codec to use for the output video in the 'Codec Selection' dialog window.
3. Click the 'Convert Video' button to start the conversion process.
4. The converted video will be saved in the same directory as the input video file with the specified FourCC codec and '.avi' file extension.

# Notes

- FourCC is a four-byte code used to specify the video codec. Here is a list of FourCC codes (https://www.free-codecs.com/guides/fourcc.htm).
- This code only supports the input video files that OpenCV can read. Here is the list of supported 
formats(https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html).
