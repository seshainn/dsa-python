
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

#  find the minimum number of steps to reduce a number n to 1 using 3 operations: subtract 1 or divide by 2 if divisible by 2 or divide by 3 if divisible by 3
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

# minimum number of perfect square numbers that sum up to a given integer n
# so, n can be represented as 1 + other_squares or 4 + other_squares or 9 + other_squares and so on. choose the one with minimum squares.
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


# minimum cost path: There is a n X m grid with cost for each cell. Find the minimum cost path to go from 0 x 0 to n-1 x m-1
def min_cost_path(matrix, i=0, j=0):
  m = len(matrix[0]) #columns
  n = len(matrix) #rows
  if i == n-1 and j == m-1:
    return matrix[i][j]
  if i == n-1:
    return matrix[i][j] + min_cost_path(matrix, i, j+1)
  if j == m-1:
    return matrix[i][j] + min_cost_path(matrix, i+1, j)
  return matrix[i][j] + min(min_cost_path(matrix, i+1, j), min_cost_path(matrix, i, j+1)) 

matrix = [[3, 2, 12, 15, 10], [6, 19, 7, 11, 17], [8, 5, 12, 32, 21], [3, 20, 2, 9, 7]]
print(min_cost_path(matrix))

def min_cost_path_dp(matrix, i=0, j=0, lookup={}):
  m = len(matrix[0]) #columns
  n = len(matrix) #rows
  if i == n-1 and j == m-1:
    return matrix[i][j]
  if i == n-1:
    if not lookup[(i, j+1)]:
      lookup[(i, j+1)] = min_cost_path_dp(matrix, i, j+1, lookup)
    return matrix[i][j] + lookup[(i, j+1)]
  if j == m-1:
    return matrix[i][j] + min_cost_path_dp(matrix, i+1, j, lookup)
  return matrix[i][j] + min(min_cost_path_dp(matrix, i+1, j, lookup), min_cost_path_dp(matrix, i, j+1, lookup)) 