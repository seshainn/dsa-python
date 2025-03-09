class Circle:
  def __init__(self, rad):
    self._r = rad
    self._area = 3.14 * rad * rad # _ denotes protected (can be accessed by child classes). However, in python it is only a naming convention and implementation is developer's responsibility.
    self.__perimeter = 3.14 * rad * 2 # __ denotes private (strictly with in class)
  
  #__str__ returns a string for the object created
  def __str__(self):
    return (f'Circle with radius {self.radius} and area {self.area}')
  #__repr__ also serves the same purpose as __str__ but is generally used for displaying debugging style messages
  
  ## When 2 objects are defined with same radius, circle1 == circle2 is actually False. circle1.radius == circle2.radius is True. Similarly circle1.area == circle2.area is True. circle1.__dict__ == circle2.__dict__ is true. To make circle1 == circle2 to be True, we need to define __eq__ dunder method.
  def __eq__(self, other):
    return self.__dict__ == other.__dict__
  
  # def get_radius(self):
  #   return self._r
  
  # def set_radius(self, radius):
  #   self._r = radius
  #   self._area = 3.14 * radius * radius

  # def del_radius(self):
  #   del self._r

  # radius = property(get_radius, set_radius, del_radius)

  @property 
  def area(self):
    return self._area 
  
  @property 
  def perimeter(self):
    return self.__perimeter 
  
  #note that the function name in all the 3 cases below is the same.
  @property
  def radius(self):
    return self._r
  
  @radius.setter
  def radius(self, new_rad):
    self._r = new_rad
    self._area = 3.14 * new_rad * new_rad
    self.__perimeter = 3.14 * new_rad * 2

  @radius.deleter
  def radius(self):
    del self._r
    del self._area
    del self.__perimeter

# Circle class in inherited by Ring class; notice the use of super()
class Ring(Circle):
  def __init__(self, radius, color, weight):
    super().__init__(radius)
    self._color = color
    self.weight = weight
  
  @property
  def color(self):
    return self._color
  @color.setter
  def color(self, value):
    self._color = value
    self._Circle__perimeter = 0 # private and protected methods can still be accessed
    self._area = 0

  @color.getter
  def color(self):
    del self._color

circle1 = Circle(7)
circle2 = Circle(7.0)
print(circle1._r) #_r is private but can still be accessed outside and by inherited children
print(circle1._Circle__perimeter) #__perimeter is private, can be accessed with name mangling (adding _Classname prefix)
print(circle1 == circle2)

ring = Ring(7, "red", 5)
print(ring.__dict__)
print(ring._Circle__perimeter)
ring.color = "yellow"
print(ring.__dict__)