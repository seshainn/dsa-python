def r_binary_search(arr, k):
  if len(arr) <= 0:
    return -1
  mid = len(arr)//2
  if arr[mid] == k:
    return mid
  elif k < arr[mid]:
    return r_binary_search(arr[:mid], k)
  else:
    index = r_binary_search(arr[mid+1:], k)
    return -1 if index == -1 else mid + 1 + index

def binary_search(arr, k):
  low = 0
  high = len(arr)-1
  while low <= high:
    mid = (low+high)//2
    if arr[mid] == k:
      return mid
    elif arr[mid] < k:
      low = mid + 1
    else:
      high = mid - 1
  return -1

def binary_search_first(arr, k):
  low = 0
  high = len(arr)-1
  result = -1
  while low <= high:
    mid = (low + high)//2
    if arr[mid] < k:
      low = mid + 1
    else:
      high = mid - 1
    if arr[mid] == k:
      result = mid

  return result
def binary_search_last(arr, k):
  low = 0
  high = len(arr)-1
  result = -1
  while low <= high:
    mid = (low + high)//2
    if arr[mid] <= k:
      low = mid + 1
    else:
      high = mid - 1
    if arr[mid] == k:
      result = mid

  return result

def binary_search_rotated(arr, k):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = (low + high)//2
    if arr[mid] == k:
      return mid
    if arr[low] > arr[mid]: #right half is sorted
      if arr[mid] < k <= arr[high]:
        low = mid + 1
      else:
        high = mid - 1
    else: #left half is sorted
      if arr[low] <= k < arr[mid]:
        high = mid - 1
      else:
        low = mid + 1
  return -1

def binary_search_rotated_min(arr):
  low, high = 0, len(arr) - 1
  while low < high:
    mid = (low + high)//2
    if arr[mid] > arr[high]: #min lies in right array
      low = mid + 1
    else: # min lies in left array (including mid)
      high = mid
  return arr[low]

def binary_search_single_among_pairs(arr):
  low, high = 0, len(arr) - 1
  while low < high:
    mid = (low + high)//2
    if mid % 2 == 1:
      mid -= 1
    if arr[mid] == arr[mid+1]:
      low = mid + 2
    else:
      high = mid
  if low > high:
    return -1
  return arr[low]

#print(r_binary_search([1, 2, 3, 4, 5, 6, 7, 8], 3))
#print(binary_search_first([1,1,2,2,2,3,4,5,6,6,7,8,9,9,9,9,9], 12))
#print(binary_search_last([1,1,2,2,2,3,4,5,6,6,7,8,9,9,9,9,9], 12))
#print(binary_search_rotated([7,8,1,2,3,4,5,6], 0))
print(binary_search_single_among_pairs([1,1,2,2,3,3,4,4,5]))