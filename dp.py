
import sys, math
# def fibonacci(n):
#   if n == 0 or n == 1:
#     return n
#   if arr[n] != -1:
#     return arr[n]
#   ans1 = fibonacci(n-1)
#   ans2 = fibonacci(n-2)
#   arr[n] = ans1 + ans2
#   return arr[n]

# n = int(input())
# arr = [-1 for i in range(n+1)]
# print(fibonacci(n))

# def min_steps(n):
#   if n == 0 or n == 1:
#     return n
#   if arr[n] != -1:
#     return arr[n]
#   ans1 = min_steps(n-1)
#   ans2 = ans3 = sys.maxsize
#   if n % 2 == 0:
#     ans2 = min_steps(n//2)
#   if n % 3 == 0:
#     ans3 = min_steps(n//3)
#   arr[n] = 1+min(ans1, ans2, ans3)
#   return arr[n]
# n = int(input())
# arr = [-1 for i in range(n+1)]
# print(min_steps(n))

def min_squares(n):
  if n == 0 or n == 1:
    return n
  if arr[n] != -1:
    return arr[n]
  arr[n] = sys.maxsize
  root = int(math.sqrt(n))
  for i in range(1, root+1):
    arr[n] = min(arr[n], 1 + min_squares(n - i**2))
  return arr[n]
  
n = int(input())
arr = [-1 for i in range(n+1)]
print(min_squares(n))
