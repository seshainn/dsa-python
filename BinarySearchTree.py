class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
        

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node=Node(value)
    if self.root == None:
      self.root=new_node
      return True
    temp=self.root
    while True:
      if new_node.value == temp.value:
        return False
      if new_node.value < temp.value:
        if temp.left == None:
          temp.left = new_node
          return True
        temp=temp.left
      if new_node.value > temp.value:
        if temp.right == None:
          temp.right = new_node
          return True
        temp=temp.right
  
  def contains(self, value):
    temp = self.root
    while temp is not None:
      if value == temp.value:
        return True
      if value < temp.value:
        temp = temp.left
      else: 
        temp = temp.right
    return False
  
  def __r_contains(self, current_node, value):
    if current_node == None:
      return False
    if value == current_node.value:
      return True
    if value < current_node.value:
      return self.__r_contains(current_node.left, value)
    if value > current_node.value:
      return self.__r_contains(current_node.right, value)
  
  def r_contains(self, value):
    return self.__r_contains(self.root, value)
  
  def __r_insert(self, current_node, value):
    if current_node == None:
      return Node(value)
    if value < current_node.value:
      current_node.left=self.__r_insert(current_node.left, value)
    if value > current_node.value:
      current_node.right=self.__r_insert(current_node.right, value)
    return current_node
  
  def r_insert(self, value):
    if self.root==None:
        self.root=Node(value)
    self.__r_insert(self.root, value)

  def min_value(self, current_node):
    while current_node.left is not None:
      current_node=current_node.left
    return current_node.value
  
  def __delete_node(self, current_node, value):
    if current_node == None:
      return None
    if value < current_node.value:
      current_node.left=self.__delete_node(current_node.left, value)
    elif value > current_node.value:
      current_node.right=self.__delete_node(current_node.right, value)
    else:
      if current_node.left == None and current_node.right == None:
        return None
      elif current_node.left == None:
        current_node=current_node.right
      elif current_node.right == None:
        current_node=current_node.left
      else:
        sub_tree_main=self.min_value(current_node.right)
        current_node.value=sub_tree_main
        current_node.right=self.__delete_node(current_node.right, sub_tree_main)
    return current_node
  
  def r_delete_node(self, value):
    self.root=self.__delete_node(self.root, value)

  def __inorder_traversal(self, current_node):
    if current_node:
      self.__inorder_traversal(current_node.left)
      print(current_node.value, end=" ")
      self.__inorder_traversal(current_node.right)
  def r_inorder_traversal(self):
    self.__inorder_traversal(self.root)

bst=BinarySearchTree()
bst.r_insert(5)
bst.r_insert(20)
bst.r_insert(3)
bst.r_insert(7)
bst.r_insert(15)
bst.r_insert(25)
bst.r_inorder_traversal()
print(" ")
print(bst.r_contains(5))
print(bst.r_contains(17))
bst.r_delete_node(5)
bst.r_inorder_traversal()