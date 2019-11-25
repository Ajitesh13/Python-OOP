#example to show to make a method abstract 

class Container:
    def __init__(self,i):
        self.x = i
    def show_volume(self):
        raise NotImplementedError("Sub classes must impliment this method")

class Cube(Container):
    def __init__(self,a):
        Container.__init__(self,a)
    def show_volume(self):
        print("Volume of the cube is " + str(self.x*self.x*self.x))

class Cuboid(Container):
    def __init__(self,l,b,h):
        self.length = l
        self.bredth = b
        self.height = h  
        Container.__init__(self,l) 
    def show_volume(self):
        print("Volume of the cuboid is "+ str(self.length*self.bredth*self.height))

c1 = Cube(5)
c1.show_volume()

c2 = Cuboid(1,2,3)
c2.show_volume()

c32 = Container(9)
c32.show_volume()