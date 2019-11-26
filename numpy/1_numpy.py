import numpy as np

#creating array object 
arr = np.array([[1,2,3],[4,5,6]])

#printing the array type
print("Array of type: " + str(type(arr)))

#printing array dimension
print("Array dimension: " + str(arr.ndim))

#printing shape of array 
print("Shape of array: " + str(arr.shape))

#printing size(no. of elements of array)
print("Size of the array is: " + str(arr.size))

#printing data types of the array
print("The array stores " + str(arr.dtype))

