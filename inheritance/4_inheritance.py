#example to show private members of a class, they will not be inherited into the child class

class Base:
    def __init__(self):
        self.x = 10
        self.__d = 42   # d is private instance variable 

class Derived(Base):
    def __init__(self):
        self.e = 84 
        Base.__init__(self)

ob1 = Derived()
print(Derived.d)