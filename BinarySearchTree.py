class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)
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
    self.root=self.__r_insert(self.root, value)

  def min_value(self):
    if self.root is None:
      return -1
    temp = self.root
    while temp.left is not None:
      temp = temp.left
    return temp.value
  
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

  def breadth_traversal(self):
    current_node = self.root
    results=[]
    queue=[]
    queue.append(current_node)

    while len(queue) > 0:
      current_node = queue.pop(0)
      results.append(current_node.value)
      if current_node.left is not None:
        queue.append(current_node.left)
      if current_node.right is not None:
        queue.append(current_node.right)
    return results

# To check if a binary tree is binary search tree: return min, max and isBST from left subtree, return min, max adn isBST from right subtree, set isBST to True if root > maxOfLST and root < minOfRST
  def r_isBST(self, root):
    if root is None:
      return float('inf'), float('-inf'), True
    
    leftMin, leftMax, leftIsBST = self.r_isBST(root.left)
    rightMin, rightMax, rightIsBST = self.r_isBST(root.right)

    if leftIsBST and rightIsBST and root.value > leftMax and root.value < rightMin:
      return min(leftMin, root.value), max(rightMax, root.value), True
    else:
      return float('-inf'), float('inf'), False

  def isBST(self):
    if self.root is None:
      return True
    treeMin, treeMax, isBinarySearchTree = self.r_isBST(self.root)
    return isBinarySearchTree

bst=BinarySearchTree()
bst.r_insert(5)
bst.r_insert(20)
bst.r_insert(3)
bst.r_insert(7)
bst.r_insert(15)
bst.r_insert(25)
bst.r_inorder_traversal()
print(" ")
print(bst.isBST())

print(bst.r_contains(5))
print(bst.r_contains(17))
bst.r_delete_node(5)
bst.r_inorder_traversal()