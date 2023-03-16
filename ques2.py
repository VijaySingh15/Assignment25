class Profile:
    def __init__(self):
        self.age=None
        self.name=None
        self.email=None
    
    def get_info(self):
        return self.name,self.age,self.email
    
    def set_info(self,name,age,email):
        self.age=age
        self.email=email
        self.name=name

p1=Profile()
p1.set_info("vijay",21,"vijaysinghnegi21@gmail.com")
print(p1.get_info())