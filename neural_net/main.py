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





if __name__ == '__main__':
	main()