# class variable and instance variable
class employee:

    companyname = "Hammer" # this is the class variable
    noemp = 0
    def __init__(self,name):
        self.name = name # this is the instance(object) variables 
        employee.noemp = employee.noemp + 1
    def showdetails(self):
        print(f"S NO.{self.noemp} The name of the emplyee is {self.name} in the {self.companyname}")


emp1 = employee("joker")
emp1.showdetails()
# we also call the method like this -> employee.showdetails(emp1){this is give the same output}
# python convert the emp1.showdetails() => employee.showdetails(emp1)

emp2 = employee("Doker")
emp2.companyname = "Hammer(india)"
# we can change the class variable like this but, 
# the class variable is same for all instance (object) untill we changed it.
# python check first instance variable and then check the class variable
emp2.showdetails()

employee.companyname="Great Hammer"
# we can change the class variable like this 
# and this is change the for all instance lekin agar kisi instance me company name kuch or set hoga to wahi print hoga
# kuyki python pehele instance variable ko check krta hai or fir class variable ko

emp3 = employee("Hokker")
emp3.showdetails()

