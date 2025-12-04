# superkey :  the super() key in python is used to refer to the parent class
# it is especially useful when a class inherites from multiple parent classes
# and you want to call a method from the parent classes
# mtlb child class me hote hue parent class se koi bhi method ko call kr sakte hai
# syntax is :   super().method_name()

class parent:
    def __init__ (self, n, i):
        self.name = n
        self.id = i
    def info(self):
        print(f"{self.name};s id is {self.id}")
    def stat(self):
        print("this is the parent method1")

class child(parent):
    def __init__(self, n, i, lang):
        self.lan = lang
        super().__init__(n, i) # use the parent constructor by super key
    def c1(self):
        print("this is the child class method 1 and parent method using super")
        super().stat() # this call the parent stat() method
        print("upper statement is  from parent class using super")
    def c2(self):
        print("this is the child class method 2")

ch = child("k",550,"python")
ch.c1() 
print(ch.lan)
print(ch.name)# print name from the parent class using the ch1 object which associated with child class

    

