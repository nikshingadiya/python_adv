class Person:
    def __init__(self,name=None,age=None):
        self.__name=name
        self.__age=age

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self,value):
        self.__name=value
    
p1=Person("Kaiju",23)
print(p1.Name)

p1.Name="yuio"

print(p1.__age)