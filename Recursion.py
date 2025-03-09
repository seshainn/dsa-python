def printNto1(n):
  if n > 0:
    print(n, end=" ")
    printNto1(n-1)

def print1toN(n):
  if n > 0:
    print1toN(n-1)
    print(n, end=" ")

# find the sum of first n natural numbers
def sumOfN(n):
  if n > 0:
    return (n + sumOfN(n-1))
  else:
    return 0

# find factorial of n
def factorial(n):
  if n == 0:
    return 1
  elif n > 0:
    return (n* factorial(n-1))
  else:
    return "Factorial does not exist for negative numbers"

def fibonacci(n):
  if n == 0 or n == 1:
    return n
  elif n > 1:
    return (fibonacci(n-1)+fibonacci(n-2))
  else:
    return "Fibonacci sequence starts with 0"

def fibSequence(n):
  for i in range(n):
    print(fibonacci(i), end=" ")

def reverse_list(my_list, left_element=0):
  right_element = len(my_list) - left_element - 1
  if left_element < right_element:
    my_list[left_element], my_list[right_element] = my_list[right_element], my_list[left_element]
    reverse_list(my_list, left_element+1)

def isPalindrome(my_str, left_index=0):
  right_index = len(my_str) - left_index - 1
  if left_index < right_index:
    if my_str[left_index] != my_str[right_index]:
      return False
    else:
      return isPalindrome(my_str, left_index+1)
  else:
    return True

print(isPalindrome("innamuri"))

def replacePi(my_str, start_index = 0):
  if start_index >= len(my_str) - 1:
    return my_str

  if my_str[start_index].lower() == 'p' and my_str[start_index + 1].lower() == 'i':
    my_str = my_str[:start_index] + "3.14" + my_str[start_index + 2:]
    return replacePi(my_str, start_index + 4)
  else:
    return replacePi(my_str, start_index + 1)

print(replacePi("piseshupigiripiinnamuri"))

def isSorted(my_list, start_index=0):
  if len(my_list[start_index:]) <= 1:
    return True
  if my_list[start_index+1] >= my_list[start_index]:
    return isSorted(my_list, start_index+1)
  else:
    return False
print(isSorted([5,5,5,5]))

def towerOfHanoi(n, left="A", middle="B", right="C", moveNum=0):
  if n > 0:
    moveNum = towerOfHanoi(n-1, left, right, middle, moveNum)
    moveNum += 1
    print(str(moveNum)+": "+"move disk "+str(n)+" from "+left+" to "+right)
    moveNum = towerOfHanoi(n-1, middle, left, right, moveNum)
  return moveNum

total_moves = towerOfHanoi(3)
print("total moves: ", total_moves)

def firstIndexOfN(n, my_list, start_index=0):
  if start_index > len(my_list) - 1:
    return -1
  if my_list[start_index] == n:
    return start_index
  else:
    return firstIndexOfN(n, my_list, start_index+1)
print(firstIndexOfN(5,[7,9,2,1,3,6,5]))

def lastIndexOfN(n, my_list, start_index=0):
  if start_index > len(my_list) - 1:
    return -1
  ind = lastIndexOfN(n, my_list, start_index+1)
  if ind == -1:
    if my_list[start_index] == n:
      ind = start_index
  return ind
print(lastIndexOfN(5,[7,9,2,1,6,8,5,0,3]))

def retAllSubsets(arr, index=0, current_subset=[]):
    if index == len(arr):
        return [current_subset]

    include_current = retAllSubsets(arr, index + 1, current_subset + [arr[index]])
    exclude_current = retAllSubsets(arr, index + 1, current_subset)

    return include_current + exclude_current

all_subsets = retAllSubsets([5,4,9])
print(all_subsets)
# for [5,4,9]:
# iter 1: 5, [] (include+exclude element at index 0)
# iter 2: 5,4; 5; 4; [] (include + exclude element at index 1 for each of iter 1)
# iter 3: 5,4,9; 5,4; 5,9; 5; 4,9; 4; 9; [] (include + exclude element at index 2 for each of iter 2)

def retAllSubsetsSumK(arr, k, index=0, current_subset=[]):
    if index == len(arr):
        if sum(current_subset) == k:
          return [current_subset]
        else:
          return []

    include_current = retAllSubsetsSumK(arr, k, index + 1, current_subset + [arr[index]])
    exclude_current = retAllSubsetsSumK(arr, k, index + 1, current_subset)

    return include_current + exclude_current
print(retAllSubsetsSumK([1,2,3,4,5,6], 6))
#list_to_reverse=[7,4,2,9,8,1,3]
#reverse_list(list_to_reverse)
#print(list_to_reverse)

#fibSequence(12)
#print(fibonacci(-1))
#print(factorial(-5))
#print(sumOfN(0))
#printNto1(20)
#print(" ")
#print1toN(20)

# iter 1: swap first with first and then swap others resulting in abc & acb
# iter 2: swap first with second and then swap others resulting in bac & bca
# iter 3: swap first with third and then swap others resulting cba & cab 
def getPermutations(my_str):
  def r_getPerm(start, end):
    if start == end:
      permutations.append("".join(arr))
      return
    for i in range(start, end):
      arr[start], arr[i] = arr[i], arr[start]
      r_getPerm(start+1, end)
      arr[start], arr[i] = arr[i], arr[start]
    
    
  arr = list(my_str)
  permutations = []
  r_getPerm(0, len(arr))
  return permutations

print(getPermutations("abcd"))



def get_permutations2(my_str):
  if len(my_str) == 0:
    return []
  if len(my_str) == 1:
    return [my_str]
  permutations = []
  for i in range(len(my_str)):
    rem_str = my_str[:i] + my_str[i+1:]
    for item in get_permutations2(rem_str):
      permutations.append(my_str[i]+item)
  
  return permutations

def combinations(arr, n):
  if n == 0:
    return [[]]
  if len(arr) < n:
    return []
  return combinations(arr[1:], n) + [[arr[0]] + combo for combo in combinations(arr[1:], n-1)]
print(combinations(['a', 'b', 'c', 'd'], 3))

def getSubSequences(my_str):
  def retAllSubsets(arr, index=0, current_subset=""):
    if index == len(arr):
      return [current_subset]
    include_current = retAllSubsets(arr, index + 1, current_subset+(arr[index]))
    exclude_current = retAllSubsets(arr, index + 1, current_subset)
    return include_current + exclude_current
  arr = list(my_str)
  all_subsets = retAllSubsets(arr)
  return all_subsets

print(getSubSequences("sehu"))

def get_string(d):
  if d == 2:
    return 'abc'
  elif d == 3:
    return 'def'
  elif d == 4:
    return 'ghi'
  elif d == 5:
    return 'jkl'
  elif d == 6:
    return 'mno'
  elif d == 7:
    return 'pqrs'
  elif d == 8:
    return 'tuv'
  elif d == 9:
    return 'wxyz'
  else:
    return ' '
def keypad_combinations(n):
  if n == 0:
    output = []
    output.append("")
    return output
  
  smallNumber = n//10
  lastDigit = n % 10

  smallerOutput = keypad_combinations(smallNumber)
  stringForLastDigit = get_string(lastDigit)

  output = []

  for s in smallerOutput:
    for c in stringForLastDigit:
      output.append(s+c)
  return output

print(keypad_combinations(23))