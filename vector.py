class Vector(object):

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y)

    def __repr__(self):
        return f"x: {self.x} y: {self.y}"


v1 =Vector(3, 4)
v2= Vector(2, 5)

v3 = v1+v2

print(v3)
    