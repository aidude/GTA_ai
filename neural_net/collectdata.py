# Collect game frames as training data and store them
# author = amritansh


import time
import cv2
import numpy as np 
from Screen_grab import screen_grab
from outputkey import output_keys_1
from getkeys import key_check
import os

path = 'D:\GTA_project_data'


starting_value = 1058

while True:
    file_name = 'training_data-{0}.npy'.format(starting_value)
    if os.path.isfile(file_name):
        print('File exists, push on!!', starting_value)
        starting_value += 1
    else:
        print('File does not exist, starting fresh!', starting_value)
break


def main(file_name, starting_value):
	training_data = []
	for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
	print('STARTING!!!')
    while True:
    	if not paused:
	    	screen = screen_grab(region=(0,40,800,640))
	    	last_time = time.time()

	    	# resize
            screen = cv2.resize(screen, (80, 60))
            # run a color convert
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            keys = key_check()
            output = output_keys_1(keys)
            training_data.append([screen,output])
            print('{} Frames per second'.format(1/(time.time()-last_time)))
        	last_time = time.time()


        	cv2.imshow('window',cv2.resize(screen,(640,360)))
	        if cv2.waitKey(25) & 0xFF == ord('q'):
	        	cv2.destroyAllWindows()
	            break


	        if len(training_data) % 100 == 0:
	        	print(len(training_data))
	        	if len(training_data) == 500:
	        		np.save(file_name, training_data)
                    print('SAVED')
                    training_data = []
                    starting_value += 1
					file_name = 'training_data-{0}.npy'.format(starting_value)

		keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('Unpaused')
                time.sleep(1)
            else:
                print('Pausing')
                paused = True
		time.sleep(1)






if __name__ == '__main__':
	main(file_name, starting_value)