class HashTable():
  def __init__(self, size=7):
    self.data_map=[None] * size

  def hash(self, key):
    total=0
    for letter in key:
      total += ord(letter) * 23
    return total % len(self.data_map)
  
  def print_table(self):
    for index, value in enumerate(self.data_map):
      print(index, ": ", value)

  def set_item(self, key, value):
    index=self.hash(key)
    if self.data_map[index]==None:
      self.data_map[index]=[]
    self.data_map[index].append([key, value])
  
  def get_item(self, key):
    index=self.hash(key)
    items=self.data_map[index]
    if self.data_map[index] is not None:
      for item in items: 
        if item[0]==key:
          return item[1]
    return None
  
  def keys(self):
    all_keys=[]
    for index, value in enumerate(self.data_map):
      if self.data_map[index] is not None:
        items=self.data_map[index]
        for item in items:
          all_keys.append(item[0])
    return all_keys
  
  

ht=HashTable()
ht.set_item("apples", 100)
ht.set_item("bananas", 96)
ht.set_item("grapes", "3kg")
ht.set_item("books", 12)
ht.set_item("pens", 5)
ht.set_item("pencils", 12)
print(ht.get_item("bolts"))
print(ht.keys())
