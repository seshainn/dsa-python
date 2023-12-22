class Node:
  def __init__(self, value):
    self.value=value
    self.next=None
    self.prev=None

class DoublyLinkedList:
  def __init__(self, value):
    self.head=Node(value)
    self.tail=self.head
    self.length = 1
  
  def print_list(self):
    temp=self.head
    while temp is not None:
      print(temp.value)
      temp=temp.next
  
  def append(self, value):
    if self.length == 0:
      self.head=Node(value)
      self.tail=self.head
    else:
      new_node=Node(value)
      self.tail.next=new_node
      new_node.prev=self.tail
      self.tail=new_node
    self.length += 1
    return True
  
  def pop(self):
    if self.length == 0:
      return None
    temp=self.head
    if self.length == 1:
      self.head=None
      self.tail=None
    else:
      while temp.next is not None:
        prev=temp
        temp=temp.next
      self.tail=prev
      self.tail.next=None
      temp.prev=None
    self.length -= 1
    return temp
  
my_dll = DoublyLinkedList(5)
print("popped value here is ", my_dll.pop().value)
my_dll.append(5)
my_dll.append(55)
print("popped value here is ", my_dll.pop().value)
my_dll.append(55)
my_dll.append(555)
my_dll.print_list()
print("popped value here is ", my_dll.pop().value)