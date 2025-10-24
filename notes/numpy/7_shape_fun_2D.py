import numpy as np

# seed is fix the output of the random number in each and every system for every time you run the programm it give the same value  
np.random.seed(5)
d= np.random.randint(1,5,[3,3])
print(d)

# the identity() function make the identity matrix it is use to make the only square matrix
c = np.identity(5)
print(c)

# the eye() function is use to make daigonal matix with 1 in daigonal and rest is 0 
d = np.eye(3,5)
# d = np.eye(5) this is also valid it give the one dimension matrix
print(f"\n{d}")

# the ones use to make the matrix with the element 1 in all postions
# e = np.ones(5)  one dimension it also valid
e = np.ones((5,1)) # two dimension requried the double brakets
print(f"\n{e}")

# the zeros use to make the matrix with the element 0 in all postions
# e = np.zeros(5)  one dimension it also valid
f = np.zeros((3,3)) # two dimension requried the double brakets
print(f"\n{f}")

