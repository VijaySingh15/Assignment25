class Calculator2:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def __mul__(self):
        return self.num1*self.num2
        
    def __div__(self):
        return self.num1/self.num2
    
class Calculator(Calculator2):
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def __add__(self):
        return self.num1 + self.num2
    
    def __sub__(self):
        return self.num1 - self.num2

c1=Calculator(5,5)
print(c1.__mul__())
print(c1.__div__())