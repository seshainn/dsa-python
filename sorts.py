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

def __r_bubble_sort(my_list, n):
  swap=False
  for j in range(n):
    if my_list[j] > my_list[j+1]:
        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        swap=True
  if swap and n > 1:
    return __r_bubble_sort(my_list, n-1)
  else:
     return my_list

def r_bubble_sort(my_list):
   n = len(my_list) - 1
   return __r_bubble_sort(my_list, n)

# Selection sort works by repeatedly finding the minimum (or maximum) element from the unsorted portion and swaps it with the element at the beginning of the unsorted list if it is smaller (for ascending order) or larger (for descending order) than the element at the current position.
def selection_sort(my_list):
  for i in range(len(my_list)-1):
    min_index = i
    swap=False
    for j in range(i+1, len(my_list)):
      if my_list[j] < my_list[min_index]:
        swap=True
        min_index = j
    if swap:
      my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
  return my_list

def __r_selection_sort(my_list, i):
  if i >= len(my_list):
    return my_list
  small_index=i
  swap=False
  for j in range(i+1, len(my_list)):
    if my_list[j] < my_list[small_index]:
      small_index=j
      swap=True
  if swap:
    my_list[i], my_list[small_index] = my_list[small_index], my_list[i]
  return __r_selection_sort(my_list, i + 1)
def r_selection_sort(my_list):
  return __r_selection_sort(my_list, 0)

# start from 2nd element in the list and keep swapping with its left element if it is less than the left element. 
def insertion_sort(my_list):
  for i in range(1, len(my_list)):
    temp=my_list[i]
    j=i
    while j > 0 and my_list[j-1] > temp:
      my_list[j]=my_list[j-1]
      j -= 1
    arr[j] = temp
  return my_list

def insertion_sort2(my_list):
  for i in range(len(my_list)-1):
    j = i+1
    while j > 0 and my_list[j] < my_list[j-1]:
      my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
      j -= 1
  return my_list


def __r_insertion_sort(my_list, i):
  if i >= len(my_list):
    return my_list
  j = i - 1
  temp=my_list[i]
  while my_list[j] > temp and j >= 0:
    my_list[j+1] = my_list[j]
    my_list[j] = temp
    j -= 1
  return __r_insertion_sort(my_list, i+1)

def r_insertion_sort(my_list):
  return __r_insertion_sort(my_list, 1)

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

# Quick sort starts with first element as Pivot and moves it to its proper position while also rearranging remaining elements such that element to left of pivot are smaller than it and elements to right of pivot are larger than it. Now the array is partitioned into two sub-arrays around the pivot, and the two sub arrays are recursively sorted until the entire list is sorted.  
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
def quick_sort(my_list):
  return quick_sort_helper(my_list, 0, len(my_list)-1)

#print(bubble_sort([2, 9, 7, 4, 8, 5, 1, 0, 3, 6]))
#print(selection_sort([2, 9, 7, 4, 8, 5, 1, 0, 3, 6]))
#print(insertion_sort([2, 9, 7, 4, 8, 5, 1, 0, 3, 6]))
#print(merge_sort([2, 9, 7, 4, 8, 5, 1, 0, 3, 6]))
print(quick_sort([2, 9, 7, 4, 8, 5, 1, 0, 3, 6]))

def in_quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr)//2]
  left = [x for x in arr if x < pivot]
  right = [x for x in arr if x > pivot]
  center = [x for x in arr if x == pivot]
  return in_quick_sort(left)+center+in_quick_sort(right)
