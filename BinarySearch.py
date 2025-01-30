def binary_search(arr, k):
  if len(arr) <= 0:
    return False
  
  mid = len(arr)//2
  if arr[mid] == k:
    return True
  elif k < arr[mid]:
    return binary_search(arr[:mid], k)
  else:
    return binary_search(arr[mid+1:], k)
  
def binary_search_index(arr, k):
  if len(arr) <= 0:
    return -1
  
  mid = len(arr)//2
  if arr[mid] == k:
    return mid
  elif k < arr[mid]:
    return binary_search_index(arr[:mid], k)
  else:
    index = binary_search_index(arr[mid+1:], k)
    return -1 if index == -1 else mid + 1 + index

print(binary_search_index([1, 2, 3, 4, 5, 6, 7, 8], 3))