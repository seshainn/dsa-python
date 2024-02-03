class Node:
  def __init__(self, value):
    self.value=value
    self.left=None
    self.right=None

class Tree:
  def __init__(self):
    self.root=None
  
  def treeInput(self):
    value=int(input())
    if value == -1:
      return None
    root=Node(value)
    root.left=self.treeInput()
    root.right=self.treeInput()
    return root
  
  def create_tree(self):
    print("Enter values inorder and -1 for None")
    self.root=self.treeInput()

  def r_printTree(self, root):
    if root == None:
      return
    print(root.value)
    self.r_printTree(root.left)
    self.r_printTree(root.right)

  def printTree(self):
    self.r_printTree(self.root)
  
  def r_printTreeDetailed(self, root):
    if root == None:
      return
    print(root.value, end=":")
    if root.left != None:
      print("L-", root.left.value, end=",")
    if root.right != None:
      print("R-", root.right.value, end="")
    print()
    self.r_printTreeDetailed(root.left)
    self.r_printTreeDetailed(root.right)

  def printTreeDetailed(self):
    self.r_printTreeDetailed(self.root)

  def r_numOfNodes(self, root):
    if root == None:
      return 0
    num1 = self.r_numOfNodes(root.left)
    num2 = self.r_numOfNodes(root.right)
    return 1 + num1 + num2
  
  def numOfNodes(self):
    return self.r_numOfNodes(self.root)

  def r_largestNode(self, root):
    if root == None:
      return -1
    
    child1 = self.r_largestNode(root.left)
    child2 = self.r_largestNode(root.right)
    return max(root.value, child1, child2)
  
  def largetsNode(self):
    return self.r_largestNode(self.root)
  
  def r_heightOfTree(self, root):
    if root == None:
      return 0
    num1 = self.r_heightOfTree(root.left)
    num2 = self.r_heightOfTree(root.right)
    return 1 + max(num1, num2)
  
  def heightOfTree(self):
    return self.r_heightOfTree(self.root)
  
  def r_numOfLeafNodes(self, root):
    if root == None:
      return 0
    
    if root.left == None and root.right == None:
      return 1
    leaves = 0
    leaves += self.r_numOfLeafNodes(root.left)
    leaves += self.r_numOfLeafNodes(root.right)
    return leaves
  
  def numOfLeafNodes(self):
    return self.r_numOfLeafNodes(self.root)
  
  def r_printNodesAtK(self, root, k):
    if root == None:
      return []
    if k == 0:
      return [root.value]
    left = self.r_printNodesAtK(root.left, k-1)
    right = self.r_printNodesAtK(root.right, k-1)
    return left+right

  def printNodesAtK(self, k):
    return self.r_printNodesAtK(self.root, k)
    
    
  

t=Tree()  
t.create_tree()

#t.printTree()
t.printTreeDetailed()
print("number of nodes: ", t.numOfNodes())
print("largest node: ", t.largetsNode())
print("height of tree: ", t.heightOfTree())
print("Number of leaf nodes: ", t.numOfLeafNodes())
print("nodes at depth 2: ", t.printNodesAtK(2))

def printSecondLine():
  print("second line")
print("first line", "\n", printSecondLine())