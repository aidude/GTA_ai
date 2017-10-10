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
    # while True:
    # 	screen = screen_grab(region=(0,40,800,640))
    # 	screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    # 	screen = cv2.resize(80,64)
    	

    while(True):
    if not paused:
        screen = grab_screen(region = (0, 40, GAME_WIDTH, GAME_HEIGHT + 40))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

        last_time = time.time()
        screen = cv2.resize(screen, (WIDTH,HEIGHT))

        delta_count_last = motion_detection(t_minus, t_now, t_plus)

        t_minus = t_now
        t_now = t_plus
        t_plus = screen
        t_plus = cv2.blur(t_plus, (4, 4))

        prediction = model.predict([screen.reshape(WIDTH,HEIGHT, 3)])[0]
        prediction = np.array(prediction) * np.array([4.5, 0.1, 0.1, 0.1, 1.8, 1.8, 0.5, 0.5, 0.2])

        mode_choice = np.argmax(prediction)

        if mode_choice == 0:
            straight()
            choice_picked = 'straight'
        elif mode_choice == 1:
            reverse()
            choice_picked = 'reverse'
        elif mode_choice == 2:
            left()
            choice_picked = 'left'
        elif mode_choice == 3:
            right()
            choice_picked = 'right'
        elif mode_choice == 4:
            forward_left()
            choice_picked = 'forward+left'
        elif mode_choice == 5:
            forward_right()
            choice_picked = 'forward+right'
        elif mode_choice == 6:
            reverse_left()
            choice_picked = 'reverse+left'
        elif mode_choice == 7:
            reverse_right()
            choice_picked = 'reverse+right'
        elif mode_choice == 8:
            no_keys()
            choice_picked = 'nokeys'
        motion_log.append(delta_count)
        motion_avg = round(mean(motion_log), 3)
        print('loop took {0} seconds. Motion: {1}. Choice: {2}'.format(round(time.time() - last_time, 3), motion_avg, choice_picked))


         # p pauses game and can get annoying.
    if 'T' in keys:
        if paused:
            paused = False
            time.sleep(1)
        else:
            paused = True
            ReleaseKey(A)
            ReleaseKey(W)
            ReleaseKey(D)
            time.sleep(1)



if __name__ == '__main__':
	main()