import numpy as np

# return the random number with in range in the form of array
a = np.random.randint(1,50,10) # 1 D
print(f"\n{a}")
print(type(a))

f = np.random.randint(1,58,[2,2]) # 2 D
print(f"\n{f}")

#for random float number/array
b = np.random.uniform(1,20,5)
print(f"\n{b}")

#other method for random float number
c = np.random.randint(1,20,2).astype(float)
print(f"\n{c}")

# ramdom number between 1 and 0
d = np.random.rand(5) #1 D
print(f"\n{d}")

e = np.random.rand(5,5) #2 D
print(f"\n{e}")


# randn generate the number close to 0 between 0 and 1 it give may be negative value -3 to 3
g = np.random.randn(5) # 1 D
print(f"\n{g}")
 
h = np.random.randn(3,3) # 2 D
print(f"\n{h}")


