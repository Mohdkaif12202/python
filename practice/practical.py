class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def find_sum(self):
        return self.a + self.b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

obj = Addition(num1, num2)
print("Sum =", obj.find_sum())
