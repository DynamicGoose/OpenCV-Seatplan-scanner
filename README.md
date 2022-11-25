# OpenCV-Seatplan-scanner
Using Python + OpenCV to scan for seats on an image of a seatplan.

# Installation and Usage

## Prerequisites
First make sure you have the latest version of Python installed on your system. To check for the newest release go to https://www.python.org/downloads/. After that, install OpenCV for Python using `pip install opencv-python`. 

## Usage
Now that you have OpenCV installed, you should be able to execute the Python script.
Upon execution, a window containing two sliders and a text field for the path to your seatplan image will appear on the screen. Type in the path to your image and press scan. If not all seats get recognized, adjust the sliders until you get the best result.
The output is saved to a .json file in the script directory in the form of pixel coordinates inside of an array. 

### If you don't know how to execute a Python script here is how to do it:
open a terminal on Linux or Command Promt on Windows and type `python /path/to/script/scanner.py`. The Window with the options for the scanner should now appear. 

**Enjoy!**
