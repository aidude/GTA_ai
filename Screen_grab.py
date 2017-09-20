# GTA 5 AI Project
# @author = amritansh

import numpy as np
from PIL import ImageGrab
import cv2

import time

def screen_record(): 
    last_time = time.time()
    while(True):
        # 800x600 windowed mode for GTA 5, at the top left position of your main screen.
        # 40 px accounts for title bar. 
        screen_capture =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        print('{} Frames per second'.format(1/(time.time()-last_time)))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(screen_capture, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()