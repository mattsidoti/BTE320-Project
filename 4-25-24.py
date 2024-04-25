class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self, other):
    x_diff = (self.x - other.x) ** 2
    y_diff = (self.y - other.y) ** 2
    return (x_diff + y_diff) ** 0.5

class Point3D(Point):
  def __init__(self, x, y, z):
    super().__init__(x,y)
    self.z = z

  def distance(self, other):
    x_diff = (self.x - other.x) ** 2
    y_diff = (self.y - other.y) ** 2
    z_diff = (self.z - other.z) ** 2
    return (x_diff + y_diff + z_diff) ** 0.5

p1 = Point(3,4)
p2 = Point(6,8)
print(p1.distance(p2))
p3 = Point3D(3, 4, 5)
p4 = Point3D(6, 8, 10)
print(p3.distance(p4))
