# This question can be solved in two ways:
# 1) without function
# 2) with Function


# without function : we just write one array with some numbers and try to find
# the largest number in the array with a few comparisons

largest_number = -1
for temp in [210, 56, 1028, 3455, 6636, 976, 0, 256] :
	if temp > largest_number :
		largest_number = temp
print("THE LARGEST NUMBER IS:" , largest_number)




# with function : we use one function which is used to compare and find a largest
#  number. the values received are the array and the lenght of array
def largestNumber(arr,n):
	max = arr[0]
	for i in range(n-1) :
		if max < arr[i] :
			max = arr[i]
	return max

arr = [210, 56, 1028, 3455, 6636, 976, 0, 256]
n = len(arr)
print("THE LARGEST NUMBER IS:" , largestNumber(arr,n))
