class Node:
  def __init__(self, value):
    self.value=value
    self.left=None
    self.right=None

class BinarySearchTree:
  def __init__(self):
    self.root=None
  
  def insert(self, value):
    new_node=Node(value)
    if self.root==None:
      self.root=Node(value)
      return True
    temp=self.root
    while True:
      if value == temp.value:
        return False
      if value < temp.value:
        if temp.left == None:
          temp.left = new_node
          return True
        temp = temp.left
      else:
        if temp.right == None:
          temp.right = new_node
          return True
        temp = temp.right
  
  def contains(self, value):
    temp=self.root
    while temp is not None:
      if value == temp.value:
        return True
      if value < temp.value:
        temp=temp.left
      else:
        temp=temp.right
    return False
    
  def r_inorder_traversal(self, curr_node):
    if curr_node:
      self.r_inorder_traversal(curr_node.left)
      print(curr_node.value, end=" ")
      self.r_inorder_traversal(curr_node.right)
  def inorder_traversal(self):
    self.r_inorder_traversal(self.root)
  


bst = BinarySearchTree()
bst.insert(7)
bst.insert(2)
bst.insert(9)
bst.insert(4)
bst.inorder_traversal()
print(" ")
#print(bst.contains(9))
#print(bst.r_contains(9))
bst.r_insert(3)
bst.inorder_traversal()
print(" ")
bst.r_insert(3)
bst.inorder_traversal()