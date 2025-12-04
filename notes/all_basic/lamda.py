# lambda function can take any number of arguments but can only have one cxpression 
# syntax => lambda arguments : expression 
# labda can take any number of argument 
#the expression is executed and the result is returned
# example
x = lambda a : a+10
print(x(5)) 
# or you can also print and call the lambda function 
# z = x(5)
# print(z)

y = lambda c,b : c*b
print(y(5,2))

z = lambda v : v>18
print(z(10))

#############################################################
# lambda function 
#  filter funtion : it returns an iterator where the items are filtered 
# through a function to test if the item is accepted or not 

# filter with function
f = [25,20,1,2,65,8,4,2,52,11,10]
def c (a):
    if a>=18:
        return True
    else:
        return False
d = list(filter(c,f))
print(f"\nfilter with function:\n{list(d)}")

# filter woth lambda function
b = list(filter(lambda age : age>18 , f))
print(f"\nfilter with lambda:\n{(b)}")
sumem = (b)
print(sumem)

# filter the even number
n = (5,2,6,7,4,88,7,41,23,6,5,8,458,5,1010)
num = filter(lambda b : b%2==0,n)
print(tuple(num))
 
# map is also same as the filter it need a function or set of data 
# map is use to transform / manuplate the each item or element in the data set 
# but filter is not use to transform but it is use to select the item form data set
ages = [2,12,54,6,8,41,25,36,52,58,9,1]
ag = list(filter(lambda x : x>10,ages))
print(list(ag))
lis = map(lambda y : y*2 , ag)
print(list(lis))

