class Heap:
  def __init__(self):
    self.HeapList = []

  def left_child(self, index):
    return 2*index + 1
  
  def right_child(self, index):
    return 2*index + 2
  
  def parent(self, index):
    return (index - 1)//2
  
  def swap(self, index1, index2):
    self.HeapList[index1], self.HeapList[index2] = self.HeapList[index2], self.HeapList[index1]

# Always insert new element at the end and keep swapping with parent if it is larger (for max heap)
  def insert(self, value):
    self.HeapList.append(value)
    current = len(self.HeapList) - 1

    while current > 0 and self.HeapList[current] > self.HeapList[self.parent(current)]:
      self.swap(current, self.parent(current))
      current = self.parent(current)
  
  def ShiftDown(self, index):
    max_index = index
    while True:
      left_index = self.left_child(index)
      right_index = self.right_child(index)

      if (left_index < len(self.HeapList) and self.HeapList[left_index] > self.HeapList[max_index]):
        max_index = left_index

      if (right_index < len(self.HeapList) and self.HeapList[right_index] > self.HeapList[max_index]):
        max_index = right_index

      if max_index != index:
          self.swap(index, max_index)
          index = max_index
      else:
          return

  def remove(self):
    if len(self.HeapList) == 0:
      return None
    if len(self.HeapList) == 1:
      return self.HeapList.pop()
    item = self.HeapList[0]
    self.HeapList[0] = self.HeapList.pop()
    self.ShiftDown(0)
    return item
  
  def heapify(self, myList):
    for i in range(len(myList)-1, 0, -1):
      self.ShiftDown(i)
  
  def print_heap(self):
    for i in self.HeapList:
      print(i, end=" ")
    print("\n")
  
heap=Heap()
heap.insert(2)
heap.insert(9)
heap.insert(7)
heap.insert(4)
heap.insert(8)
heap.print_heap()
print(heap.remove())
heap.print_heap()