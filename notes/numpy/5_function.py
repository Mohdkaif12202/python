import numpy as np
a=[[1,2,3],[4,5,6],[7,8,9]]
mat= np.array(a)
print(mat)
print(mat.ndim) #dimension

print(mat.shape)#shape (order of matrix)

print(mat.size) # give the number of element in matrix

print(mat[2:,0:1]) # slicing of the 2d matrix

print(mat.max()) # find the max number in the matrix

print(mat.min()) # find the min number in the matrix

print(mat.mean()) # find the mean of the number in the matrix

print(mat.sum()) # find the sum of the number in the matrix

print(mat.prod()) # find the simple product number in the matrix. It dont give the real matrix product

b = np.zeros(mat.shape) # convert the all element into zeros in the matrix
print(b)

b = np.ones(mat.shape) # find the order of the matrix 
print(f"\n{b}")

print(mat.reshape(9)) # convert the 2d into 1d or 1d into 2d array lekin total element hone chahiye conversion ke baad or pehele bhi

l= mat.reshape(1,-1) # minus one(-1) concept in this on the place of the -1 system will calculate itself but other is must be product of the total elements
print(l)


