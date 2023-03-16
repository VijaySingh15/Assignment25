class Person:
    def __init__(self):
        self._name=None
        self.__age=None
        self.__email=None
    
    def set_info(self,name,age,email):
        self._name=name
        self.__age=age
        self.__email=email
    
    def get_info(self):
        return self._name,self.__age,self.__email
    
p1=Person()
p1.set_info("Vijay",21,"negivijaysingh15@gmail.com")
print(p1.get_info())