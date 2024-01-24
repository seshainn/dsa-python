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