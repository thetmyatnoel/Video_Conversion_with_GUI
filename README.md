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

# Acknowledgements

This code is a Python script that allows the user to select an input video file and a FourCC codec to use for the output video file using a graphical user interface (GUI) provided by the tkinter library.

The script first imports the necessary libraries, including OpenCV for video processing and tkinter for creating the GUI. It then defines two functions, get_video_file and get_codec, that open file dialogs to allow the user to select the input video file and enter the FourCC codec, respectively.

Once the input video file and codec are selected, the script uses OpenCV to read the video file and create a VideoWriter object to write the output video file with the specified codec. The script then iterates through each frame of the input video, writes each frame to the output video, and saves the output video file to disk.

To use the script, the user must simply run it in a Python environment and follow the prompts in the GUI to select the input video file and codec. The output video file will be saved in the same directory as the input video file with the specified codec and the file extension ".avi".

The script can be useful for anyone who needs to process large video files and wants a simple way to select the input file and codec without having to manually enter command line arguments or modify the code. It can also serve as a good starting point for building more complex video processing scripts that utilize the OpenCV library.





