#example showing invoking of parent class constructer in the child class

class Base:
    def __init__(self, i):
        self.x = i
    def get_x(self):
        print(str(self.x))

class Derived(Base):
    def __init__(self,i,j):
        self.y = j
        Base.__init__(self,i)
    def get_y(self):
        print(str(self.y))

bob = Base(5)
bob.get_x()

dob = Derived(2,3)
dob.get_x()
dob.get_y()