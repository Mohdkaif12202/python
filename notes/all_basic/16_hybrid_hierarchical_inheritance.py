# hybrid inheritance 
# it is the combination of the multiple inheritance and single inheritance in oops
# this is the example of the hybrid inheritance
class baseclass:
    pass

class derivaed1(baseclass):
    pass

class derived2(baseclass):
    pass

class derived3(derivaed1,derived2):
    pass
#==========================================
#this is the hierarchical inheritance example
class base():
    pass
class p1(base):
    pass
class p2(base):
    pass
class p3(p1):
    pass
class p4(p2):
    pass
