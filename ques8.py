class Calculator2:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def __mul__(self):
        print(self.num1*self.num2)
        
    def __div__(self):
        print(self.num1/self.num2)
    
class Phone:
    def features1(self):
        print("Calling....")
    def features2(self):
        print("SMS....")    

class Smartphone(Calculator2,Phone):
    pass

sP=Smartphone(5,5)
sP.features1()
sP.__mul__()

