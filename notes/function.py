def fact(a):
    if a==1 or a==0:
        return 1
    elif a<1:
        print("enter the valid number")
    else:
        c=a*fact(a-1)
        return c
b=int(input("enter the number"))
print(fact(b))