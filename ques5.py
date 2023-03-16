class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def __add__(self):
        return self.num1 + self.num2
    
    def __sub__(self):
        return self.num1 - self.num2
    
c1=Calculator(4,3)
print(c1.__add__())
print(c1.__sub__())