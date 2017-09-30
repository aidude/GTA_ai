import pyautogui
from directkeys import PressKey, ReleaseKey, W, A, S, D

# class Movement(object):
#     """docstring for Movement"""
#     def __init__(self, arg):
#         super Movement, self).__init__()
#         self.arg = arg
        

def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def left():
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)
    ReleaseKey(A)

def right():
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(W)
    ReleaseKey(D)

def slow_up():
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def accelerate():
    PressKey(W)


# if __name__ == '__main__':
   