class Circle:
  def __init__(self, radius):
    self._r = radius
    self._area = 3.14 * radius * radius
  
  def get_radius(self):
    return self._r
  
  def set_radius(self, radius):
    self._r = radius
    self._area = 3.14 * radius * radius

  def del_radius(self):
    del self._r

  radius = property(get_radius, set_radius, del_radius)
  
  @property
  def area(self):
    return self._area
  #@area.setter is skipped
  @area.deleter
  def area(self):
    del self._area
  
c = Circle(7)
print(c.radius, c.area)
print(c.__dict__)
c.radius = 3.5
print(c.__dict__)
print(c.area)
del c.radius
del c.area
print(c.__dict__)