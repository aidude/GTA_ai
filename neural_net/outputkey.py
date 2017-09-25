# author = amritansh

from directkeys import W, A, D, directkeys

def output_keys(keys):
	output_array = [0,0,0]

	if 'A' in keys:
		output_array[0] = 1
	elif 'D' in keys:
		output_array[2] = 1
	else:
		output_array[1] = 1
	return output_array
