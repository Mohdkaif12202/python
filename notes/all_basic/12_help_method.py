# there have three help method : 
# dir(), __dict__, help()

# dir(): this function returns a list of all the attributes and methods available for an object
# it is a useful tool for discobering what you can do with an object

# __dict__ : it return the dictionary representation of an object's attributes 
# it is use full for the introspection

# help(): this function use to get help documentation for an object
# including a description of its attribures and methods
class employee:
    def __init__ (self , n , i):
        self.name = n
        self.id = i
    def info(self):
        print(f" The employee {self.name}'s id is {self.id} ")
    
a = employee("k" , 501)
a.info()

b=[]
print(dir(b)) # print the all list method which we can apply
print(a.__dict__) # print all attribute in form of the dictionary
print(help(a)) # it return the all detail of the object