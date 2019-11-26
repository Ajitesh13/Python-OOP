#example to show multilevel inheritance and parent-child-grandchild class relationships

class Base:
    def __init__(self,i):
        print("Base constructer called")
        self.x = i
    def get_x(self):
        print("x = " + str(self.x))

class Derived1(Base):
    def __init__(self,i,j):
        print("Derived1 constructer called")
        self.y = j
        Base.__init__(self,i)
    def get_y(self):
        print("y = " + str(self.y))

class Derived2(Derived1):
    def __init__(self,i,j,k):
        print("Derived2 constructer callled")
        self.z = k
        Derived1.__init__(self,i,j)
    def get_z(self):
        print("z = " + str(self.z))

ob1 = Base(5)

ob1.get_x()

ob2 = Derived1(1,2)
ob2.get_y()
ob2.get_x()

ob3 = Derived2(6,7,8)
ob3.get_z()
ob3.get_x()
ob3.get_y()