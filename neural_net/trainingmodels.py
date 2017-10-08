# training our models
# author = amritansh


import numpy as np
import os
import cv
import pandas as pd

from grabscreen import grab_screen
from tqdm import tqdm
from collections import deque
from models import inception_v3 as googlenet
from random import shuffle


FILE_END = 1080
WIDTH = 80
HEIGHT = 60

EPOCHS = 25

LR = 1e-2

LOAD_MODEL = True

PREV_MODEL = ''
MODEL_NAME = ''

model = googlenet(WIDTH, HEIGHT, 3, LR, output=9, model_name = MODEL_NAME)

if LOAD_MODEL:
    model.load(PREV_MODEL)
print('We have loaded a previous running model !!')


for epoch in range(EPOCHS):
	data_order = [i for i in range(1, FILE_I_END + 1)]
	shuffle(data_order)
	for count,i in enumerate(data_order):
		try:
			file_name = 'D:/phase10-random-padded/training_data-{0}.npy'.format(i)
            # full file info
            train_data = np.load(file_name)
		print('training_data-{0}.npy'.format(i), len(train_data))

		train = train_data[:-50]
        test = train_data[-50:]

        X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 3)
        Y = [i[1] for i in train]

        test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 3)
        test_y = [i[1] for i in test]

        model.fit({'input': X}, {'targets': Y}, n_epoch = 1, validation_set = ({'input': test_x}, {'targets': test_y}),
            snapshot_step = 2500, show_metric = True, run_id = MODEL_NAME)

        if count % 10 == 0:
            print('SAVING MODEL!')
            model.save(MODEL_NAME)

    except Exception as e:
        print(e)
