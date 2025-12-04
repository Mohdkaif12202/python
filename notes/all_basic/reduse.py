'''reduce() function: Comes from the functools module and is used to apply
a rolling computation to sequential elements in a list.'''

'''to use the reduce() function you firstly import the functools '''

'''Examples Demonstrated:
Using reduce() to calculate the sum or product of elements in a list.'''

from functools import reduce
no =[1,2,3,4,5]
k = (reduce(lambda r,j : r*j, no))
print(k)

'''finding the max number in the list using reduce() function'''
val = [5,2,4,5,1,8,9,75,1,0]
k = reduce(lambda a,b : a if a>b else b,val)
print(f"the max number is : {k}")

# min number
min = reduce(lambda a,b : a if a<b else b , val)
print(f"the min number is : {min}")