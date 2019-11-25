#example showing multiple inheritance and parent-constructer invoking in child class

class Base1:
    def __init__(self,i):
        print("Base1 constructer called")
        self.x = i
    def get_x(self):
        print("x = " + str(self.x))
    
class Base2:
    def __init__(self,j):
        print("Base2 constructer called")
        self.y = j
    def get_y(self):
        print("y = " + str(self.y))

class Derived(Base1,Base2):
    def __init__(self,i,j,k):
        print("Derived constructer called")
        self.z = k
        #invoking the constructer of base1 and base2
        Base1.__init__(self,i)
        Base2.__init__(self,j)
    def get_z(self):
        print("z = " + str(self.z))
    def get_everything(self):
        print("x = " + str(self.x) + " y = " + str(self.y) + " z = " + str(self.z))

#driver code
ob1 = Base1(5)
ob1.get_x()

ob2 = Base2(6)
ob2.get_y()

ob3 = Derived(7,8,9)
ob3.get_x()
ob3.get_y()
ob3.get_z()
ob3.get_everything()
