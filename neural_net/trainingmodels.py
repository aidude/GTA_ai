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