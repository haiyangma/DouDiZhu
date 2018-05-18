import os
import subprocess
import sys
import cv2
import numpy as np




def getScreenshot():
    process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE, bufsize=1)
    screenshot = process.stdout.read()
    if screenshot == b'':
        print('Please make sure you can run adb commands successfully.')
        os._exit(0)
    if sys.platform == 'win32':
        screenshot = screenshot.replace(b'\r\n', b'\n')
    return cv2.imdecode(np.fromstring(screenshot, np.uint8), 0)