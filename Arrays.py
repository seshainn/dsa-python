# remove duplicates from a sorted list
def remove_dups_sortedList(my_list):
  i = 0
  for j in range(1, len(my_list)):
    if my_list[j] != my_list[i]:
      i += 1
      my_list[i] = my_list[j]
  # do not use pop() to remove remaining items using for j in range(i+1, len(my_list)) becuase length of my_list changes with every pop and for loop gets executed as per original length resulting in out of range error
  return my_list[:i+1]

def reverse(my_list):
  start=0
  end=len(my_list)-1
  while start < end:
    my_list[start], my_list[end] = my_list[end], my_list[start]
    start += 1
    end -= 1
  return my_list
print(reverse([2,7,9,4,0,6,3,8]))

# left rotate a list by k elements, using extra space
def left_rotate_by_k(my_list, k):
  temp=my_list[:k]
  my_list=my_list[k:]
  for item in temp:
    my_list.append(item)
  return my_list
print(left_rotate_by_k([2,7,9,4,0,6,3,8], 3))

# left rotate a list by k elements without using extra space
def opt_left_rotate_by_k(my_list, k):
  def sub_reverse(my_list, start, end):
    while start < end:
      my_list[start], my_list[end] = my_list[end], my_list[start]
      start += 1
      end -= 1

  k = k % (len(my_list))
  sub_reverse(my_list, 0, k-1)
  sub_reverse(my_list, k, len(my_list)-1)
  sub_reverse(my_list, 0, len(my_list)-1)
  return my_list
print(opt_left_rotate_by_k([2,7,9,4,0,6,3,8], 7))

# An array should contain first n natural numbers but one of them is missing. Find it.
# hint: calculate sum of elements in the array and subtract it from n(n+1)/2

# An array has zeros dispered across. Move all zeros to the end.
# hint: use two pointers. First pointers traverses from start to end. When zero is found, use a second pointer. Move the first pointer to next non-zero value and swap with second pointer's zero. Move second pointer to next zero found. 

# find longest sub-array with sum k
# hint: use 2 pointers with both at start element. Now sub-array has single element. If sub-array sum is less than k, increase foward pointer ahead to increment sub-array elements by 1. if sub-array sum is more than k, drop the left most element from sub-array by moving back pointer ahead.

# find 2 elements in an array that give a sum k
# hint: use dictionary/hashmap to store the elements as they are read. For each element read, check existing elements of hashmap if there exists an element that gives a sum k.

# sort an array which has 3 distinct elements (preferably 0, 1 and 2)
# hint: use 3 pointers, low, mid, high where low=mid=0 and high=len-1. if list[mid] = 0, swap with list[low] and increment both indices. if list[mid] = 1, increment mid. if list[mid] = 2, swap with high and decrement high. This is called dutch flag algorithm.


                         

#print(remove_dups_sortedList([1,1,1,2,2,4,5,5,5,5,5,7,8,9,9,9]))
