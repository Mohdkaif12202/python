class shape:
    def __init__ (self, x, y):
        self.x =x
        self.y =y
    def area(self):
        return self.x *self.y
    
class circle(shape):
    def __init__(self,radius):
        # self.r = radius
        super().__init__(radius, radius)
        
    def area(self):
        return 3.14 * super().area() # overriding the shape class area in child class
c = circle(5)
print(c.area())

# Method overriding in Python is the process of redefining a method
# of the parent class in the child class, so that the
# child class can provide its own specific implementation of that method

# (Jab child class parent class ke method ko dobara define karti hai apni 
# requirement ke hisaab se, usse method overriding kehte hain)  