class Truecaller:
    def __init__(self):
        self.name=None
        self.number=None
        
    def fetch(self,other):
        d1={self.name:self.number,other.name:other.number}        
        return d1

    def new_entry(self,name,number):
        self.name=name
        self.number=number

class Smartphone(Truecaller):
    def features1(self):
        print("Calling....")
    def features2(self):
        print("SMS....") 
        

tC=Truecaller()
tC1=Truecaller()
tC2=Truecaller()
tC1.new_entry("akku",9315772105)
tC.new_entry("Vijay",9871180664)
tC2.new_entry("Nikhil",837339320)
print(Smartphone.fetch(tC,tC1))
