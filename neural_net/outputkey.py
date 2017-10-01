# author = amritansh

from directkeys import W, A, D, directkeys




def output_keys(keys):
	key_map = [0,0,0]

	if 'A' in keys:
		output_array[0] = 1
	elif 'D' in keys:
		output_array[2] = 1
	else:
		output_array[1] = 1
	return key_map

def output_keys_1(keys):
	""" Create one hot encoding and tack them together
	"""

	key_map = {
    'W': [1, 0, 0, 0, 0, 0, 0, 0, 0],
    'S': [0, 1, 0, 0, 0, 0, 0, 0, 0],
    'A': [0, 0, 1, 0, 0, 0, 0, 0, 0],
    'D': [0, 0, 0, 1, 0, 0, 0, 0, 0],
    'WS': [0, 0, 0, 0, 1, 0, 0, 0, 0],
    'WD': [0, 0, 0, 0, 0, 1, 0, 0, 0],
    'SA': [0, 0, 0, 0, 0, 0, 1, 0, 0],
    'SD': [0, 0, 0, 0, 0, 0, 0, 1, 0],
    'NK': [0, 0, 0, 0, 0, 0, 0, 0, 1],
    'default': [0, 0, 0, 0, 0, 0, 0, 0, 0],
	}
	if ''.join(keys) in key_map:
        return key_map[''.join(keys)]
	return key_map['default']

