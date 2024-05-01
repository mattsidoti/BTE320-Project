class point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def distance(self,other):
    x_diff=(self.x-other.x)**2
    y_diff=(self.y-other.y)**2
    return (x_diff+y_diff)**.05

p1=point(3,4)
p2=point(6,8)
print(p1.distance(p2))

class point3D(point):
  def __init__(self,x,y,z):
    super().__init__(x,y)
    self.z=z
  def distance(self,other):
    x_diff=(self.x-other.x)**2
    y_diff=(self.y-other.y)**2
    z_diff=(self.z-other.z)**2
    return (x_diff+y_diff+z_diff)**.05

p3=point3D(3,4,6)
p4=point3D(5,6,8)
print(p3.distance(p4))