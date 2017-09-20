# GTA 5 AI Project
# @author = amritansh



import math
import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import PressKey, W, A, S, D



def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0],coords[1]), (coords[2],coords[3]), [255,255,255], 3)
    except:
        pass

def process_img(image):
    original_image = image
    # convert to gray
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_image = cv2.Canny(processed_image, threshold1 = 200, threshold2=300)
    # Guassian Blur
    processed_image = cv2.GaussianBlur(processed_image, (5,5), 0)
    # Hough lines 
    lines = cv2.HoughLinesP(processed_image, np.pi/180, 180, 20, 0)
    draw_lines(processed_image, lines)
    return processed_image


def roi(image, vertices):
    mask = np.zeroes_like(image)
    cv2.fillPoly(mask, vertices, 255)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def main():
    
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    while True:
        # PressKey(W)
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        print('{} Frames per second'.format(1/(time.time()-last_time)))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()