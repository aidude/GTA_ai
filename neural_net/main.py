# GTA 5 AI Project
# author = amritansh


import time
import cv2
import numpy as np 
from Screen_grab import screen_grab
from outputkeys import output_keys
from getkeys import key_check

import os

path = 'D:\GTA_project_data'

file_name = 'training_data.npy' 


if os.path.isfile(file_name):
	print('File Exists, Fetching data !')
	training_data = list(np.load(file_name))
else:
	print('File does not exists, try again !')
	training_data = []



def main():
	for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    while True:
    	screen = screen_grab(region=(0,40,800,640))
    	screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    	screen = cv2.resize(80,64)
    	

        while(True):
        if not paused:
            screen = grab_screen(region = (0, 40, GAME_WIDTH, GAME_HEIGHT + 40))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

            last_time = time.time()
            screen = cv2.resize(screen, (WIDTH,HEIGHT))




if __name__ == '__main__':
	main()