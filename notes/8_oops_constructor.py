class detail:
    def __init__(self , n , r , c): # this is the constructor and it take the one argument automaticly and other come based on the need 
        self.name = n
        self.roll_num = r # this self with the variable is nessary
        self.clas = c

    def info(self): # this self is nessary in this function (method of the detail)
        print(f"name is {self.name}\nroll number is = {self.roll_num}\nclass is {self.clas}")

k= input("enter the name")
n=int(input("num= "))
d=int(input("class= "))
a = detail(k,n,5) # this take the k and n based on the user input and other is 5 like default
# a.info()
# print(a.name , a.roll_num, a.clas)
# a = detail("k",5,5)
a.info() # call the info function
a.name = "kif" # change the name and all other based on the user
a.info()
print(a.name) # only print the name 

######################################
# constructor has two type 
# 1.parameterized constructor ==> when the constructor accrpts argument along with the self
# 2.default construction ==> when the constructor donesn't take any argument from object and take only one argumeny (self)

