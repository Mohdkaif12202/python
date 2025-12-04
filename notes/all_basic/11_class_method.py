class car:
    company = "honda"
    def __init__(self,m,c):
        self.model = m
        self.colore = c

    def info(self): 
        print(f"The model of the car is {self.model},and The color is {self.colore}")
        print(f"the company of car is : {self.company}")

    @classmethod
    def change(cls,v):
        cls.company = v
    # by the class method we can change the class variable directly 
    # to use the class method you simply use the "@classmethod" befor the method defination 
    # the first argument is the "cls" which represent the class it self

c1 = car(2024,"red")
c1.info()
c1.change("pluser") # changing the value of class variable
c1.info() 
print(car.company)