# getter is use for get the value it is the safe method to read the value  of a private variable in a class
# it help to implement the incapsulation - a core concept og oops that hide the internal data and controle how its accessed or modified
# data protection
# validation 
# maintence - on chaning the validation condition , you only need to update the setter section without change the source code of class
class person:
        
        def __init__(self , n ,a):
            self.name = n
            self.age = a            
        # def get_age(self): #  this is getter without using @property  and this is unsafe 
        #     return self.age
        @property  # this is the getter withh @property in pythonic way or this is the safe way to get the value
        def ages(self):
            return (self.age -10 )
        
p = person("kaif" , 45) # creating the object of the class person

# p.age = 54 this will change the value of the age

print(f"{p.name}'s age is : {p.ages} \nThis is called by def __init__ statement \n ")  # this call the age vaue from the def __init__

print(f"{p.name}'s age is : {p.ages} \nThis is called by property statement \n") # this call the age value from the property


##################################################################################

# setter - it is a method that controle how a private attribute value is change 
# it provide the vaidation data and trigger update or side effect befor actually assiging a value
# You can only use a setter if a property has already been declared with @property

# with out setter (unsafe) anyone can assign the any nonsence value which has no meaning and logic 
class school:
    def __init__(self , name , marks):
          self._name = name
          self._marks = marks
    
    # def info (self):
    #      print(f"{self._name}'s marks is :> {self._marks}")


    @property # (getter)
    def _markss (self): # defination of the property (_markss) is same as the name of the setter (@ anme of the def in property) and also def of the setter
         return self._marks 
    
    @_markss.setter # (setter)
    def _markss (self,value):
        if value > 0:
              self._marks = value
        else:
            print("enter the logical value \nprevious value is :")
              
    def info (self):
         print(f"{self._name}'s marks is :> {self._marks}")
    
s = school("k",500)
x = int(input ("enter the marks:\n"))
s._markss = x # like this any non sence value can add 
s.info()

# imp notes -> setter tabhi kaam krega jab gettter bana hoga , getter or setter dono me same name hona chahiye def ka , 