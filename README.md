# OpenCV-Seatplan-scanner
Using Python + OpenCV to scan for seats on an image of a seatplan.

# Installation and Usage

## Prerequisites
First make sure you have the latest version of Python installed on your system. To check for the newest release go to https://www.python.org/downloads/. After that, install OpenCV for Python using `pip3 install opencv-python`. 

## Usage
Now that you have OpenCV installed, you should be able to execute the Python script by typing `python /path/to/script/scanner.py` in your terminal.
Upon execution, a window containing two sliders and a text field for the path to your seatplan image will appear on the screen. Type in the path to your image and press scan. If not all seats get recognized, adjust the sliders until you get the best result.
The output is saved to a .json file in the script directory in the form of pixel coordinates inside of an array. 

## Tips
### Tkinter import error (Linux):
If you get an error importing tkinter Tk might not be installed. Use your distributions package manager to install it.
- **Arch**: `sudo pacman -S tk`
- **Debian**: `sudo apt-get install python3-tk`
- **Fedora**: `sudo dnf install python3-tkinter`
- **Ubuntu**: `sudo apt install python3-tk`
### Pip not found
Pip might not be installed: `python -m pip install --upgrade pip`\
If Pip is installed but still doesn't work, try adding it to your `PATH`:
- **Linux**: `export PATH=$PATH:/path/to/pip` These changes aren't permanent. If you want them to be you'll have to add the command to the end of your .bashrc file.
- **Windows**: Search for environment variables in the start-menu and open the utility. Add the path to Pip to the `PATH` environment variable. 

**Enjoy!**
