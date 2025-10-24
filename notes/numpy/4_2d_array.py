import numpy as np
a=[]
r= int(input("enter the row = "))
c= int(input("enter the clomun = "))
for i in range(r):
    b=[]
    for j in range(c):
        n= int(input("enter the element = "))
        b.append(n)
    a.append(b)
matrix= np.array(a)
print(f"matrix : \n{matrix}")

for i in range(r):
    for j in range(c):
        print(a[i][j] ,end=" ")
    