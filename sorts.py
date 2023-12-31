# Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order, continuing until the entire list is sorted.
def bubble_sort(my_list):
  for i in range(len(my_list) - 1, 0, -1):
    swapped=False
    for j in range(i):
      if my_list[j] > my_list[j+1]:
        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        swapped=True
    if not swapped:
      break
  return my_list

# Selection sort works by repeatedly finding the minimum (or maximum) element from the unsorted portion and swaps it with the element at the beginning of the unsorted list if it is smaller (for ascending order) or larger (for descending order) than the element at the current position.
def selection_sort(my_list):
  for i in range(len(my_list)-1):
    swap=False
    temp=my_list[i]
    for j in range(i+1, len(my_list), 1):
      if my_list[j] < temp:
        temp=my_list[j]
        swap_ind=j
        swap=True
    if swap:
      my_list[i], my_list[swap_ind] = my_list[swap_ind], my_list[i]
  return my_list

# start from 2nd element in the list and keep swapping with its left element if it is less than the left element. 
def insertion_sort(my_list):
  for i in range(1, len(my_list)):
    temp=my_list[i]
    j=i-1
    while temp < my_list[j] and j >= 0:
      my_list[j+1]=my_list[j]
      my_list[j]=temp
      j -= 1
  return my_list

# Merge sort divides the unsorted list into smaller sublists until each sublist had a single element, recursively sorts these sublists, and merges them back together in a sorted manner.
def merge_sort(my_list):
  def merge(list1, list2):
    combined=[]
    i = j = 0
    while i < len(list1) and j < len(list2):
      if list1[i] < list2[j]:
        combined.append(list1[i])
        i += 1
      else:
        combined.append(list2[j])
        j += 1
    while i < len(list1):
      combined.append(list1[i])
      i += 1
    while j < len(list2):
      combined.append(list2[j])
      j += 1
    return combined
  
  if len(my_list) == 1:
    return my_list
  
  mid_index=int(len(my_list)/2)
  left=merge_sort(my_list[:mid_index])
  right=merge_sort(my_list[mid_index:])
  return merge(left, right)

# Quick sort selects a pivot element, partitions the array into two sub-arrays around the pivot, and recursively sorts the sub-arrays until the entire list is sorted.  
def quick_sort(my_list):
  def pivot(my_list, pivot_index, end_index):
    swap_index=pivot_index
    for i in range(pivot_index+1, end_index+1):
      if my_list[i] < my_list[pivot_index]:
        swap_index += 1
        my_list[swap_index], my_list[i] = my_list[i], my_list[swap_index]
    my_list[swap_index], my_list[pivot_index] = my_list[pivot_index], my_list[swap_index]
    return swap_index
  
  def quick_sort_helper(my_list, left, right):
    if left < right:
      pivot_index = pivot(my_list, left, right)
      quick_sort_helper(my_list, left, pivot_index - 1)
      quick_sort_helper(my_list, pivot_index+1, right)
    return my_list
  
  return quick_sort_helper(my_list, 0, len(my_list)-1)

#print(bubble_sort([2, 9, 7, 4, 8, 5, 1, 0, 3, 6]))
#print(selection_sort([2, 9, 7, 4, 8, 5, 1, 0, 3, 6]))
#print(insertion_sort([2, 9, 7, 4, 8, 5, 1, 0, 3, 6]))
#print(merge_sort([2, 9, 7, 4, 8, 5, 1, 0, 3, 6]))
print(quick_sort([2, 9, 7, 4, 8, 5, 1, 0, 3, 6]))