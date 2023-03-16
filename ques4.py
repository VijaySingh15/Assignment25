class Profile:
    
    platform="Ineuron"
    
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
    
    @classmethod
    def class_variable(cls):
        return cls.platform
    
p1=Profile()
print(Profile.class_variable())