'''
Maximum subarray problem is an problem in which we have to find a contiguous subarray
having max sum.
For eg. 
Suppose here's an array - [0,5,8,-3,-1,6,12,-13]
Then sub-array(contiguous) with largest sum is 27

Below is it's implementation in Python.
'''

def maxSub(arr):
	max_of_all = 0
	max_current = 0

	#uses Python built-in funtion max()
	for element in arr:
		max_current = max(0, max_current+element)
		max_of_all = max(max_current, max_of_all)

	return max_of_all

#Test
print maxSub([0,5,8,-3,-1,6,12,-13])