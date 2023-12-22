class Node:
  def __init__(self, value):
    self.value=value
    self.next=None

class LinkedList:
  def __init__(self,value):
    self.head=Node(value)
    self.tail=self.head
    self.length = 1

  def print_list(self):
    node = self.head
    while node is not None:
      print(node.value)
      node=node.next

  def append(self, value):
    if self.length == 0:
      self.head=Node(value)
      self.tail=self.head
      self.length = 1
    else:
      new_node=Node(value)
      self.tail.next=new_node
      self.tail=new_node
      self.length += 1
    return True
  
  def pop(self):
    if self.length == 0:
        return None
    elif self.length == 1:
        value = self.head.value
        self.head = None
        self.tail = None
        self.length = 0
        return value
    else:
      currnode=self.head
      prevnode=self.head
      while currnode.next is not None:
        prevnode=currnode
        currnode=currnode.next
      self.tail=prevnode
      self.tail.next=None
      self.length -= 1
      return currnode.value
    
  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    else:
      node=self.head
      for i in range(index):
        node = node.next
      return node
    
  def set(self, index, value):
    temp = self.get(index)
    if temp:
      temp.value=value
      return True
    return False
  
  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return True
  
  def pop_first(self):
    if self.length == 0:
        return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
        self.tail = None
    return temp
  
  def insert(self, index, value):
    if index < 0 or index > self.length:
      return False
    elif index == self.length:
      return self.append(value)
    elif index == 0:
      return self.prepend(value)
    else:
      new_node = Node(value)
      temp=self.get(index-1)
      new_node.next=temp.next
      temp.next=new_node
    self.length += 1
    return True

  def remove(self,index):
    if index < 0 or index >= self.length:
        return None
    if index == 0:
        return self.pop_first()
    if index == self.length - 1:
        return self.pop()
    pre = self.get(index - 1)
    temp = pre.next
    pre.next = temp.next
    temp.next = None
    self.length -= 1
    return temp
  
  def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp

    after = temp.next
    before = None
    for _ in range(self.length):
        after = temp.next
        temp.next = before
        before = temp
        temp = after

my_ll = LinkedList(2)
print("pop value is ", my_ll.pop())
my_ll.append(4)
my_ll.append(7)
my_ll.append(29)
my_ll.append(12)
my_ll.print_list()
print("value at index 2 is ", my_ll.get(2).value)
my_ll.set(2, 9)
my_ll.print_list()
my_ll.reverse()
my_ll.print_list()