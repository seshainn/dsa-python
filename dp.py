def fibb(n):
  if n == 0 or n == 1:
    return n
  if fiblist[n-1] == -1:
    ans1 = fibb(n-1)
    fiblist[n-1] = ans1
  else:
    ans1 = fiblist[n-1]
  if fiblist[n-2] == -1:
    ans2 = fibb(n-2)
    fiblist[n-2] = ans2
  else:
    ans2 = fiblist[n-2]
  
  return ans1+ans2

n=12
fiblist = [-1 for i in range(n+1)]
print(fibb(n))

def fibbI(n):
  fibseq = [0 for i in range(n+1)]
  fibseq[1] = 1
  for i in range(2, n+1):
    fibseq[i] = fibseq[i-1] + fibseq[i-2]
  
  return fibseq[n]

print(fibbI(10))

import sys
def minStepsTo1(n):
  if n == 1:
    return 0
  
  ans1 = ans2 = ans3 = sys.maxsize
  if minStepsList[n-1] == -1:
    ans3 = minStepsTo1(n-1)
    minStepsList[n-1] = ans3
  else:
    ans3 = minStepsList[n-1]

  if n%2 == 0:
    if minStepsList[n//2] == -1:
      ans1 = minStepsTo1(n//2)
      minStepsList[n//2] = ans1
    else:
      ans1 = minStepsList[n//2]

  if n%3 == 0:
    if minStepsList[n//3] == -1:
      ans2 = minStepsTo1(n//3)
      minStepsList[n//3] = ans2
    else:
      ans2 = minStepsList[n//3]
  
  return (1 + min(ans1, ans2, ans3))

n=20
minStepsList = [-1 for i in range(n+1)]
print(minStepsTo1(n))

import sys
def minStepsTo1I(n):
  minStepsList = [-1 for i in range(n+1)]

  for i in range(1, n+1):
    if i == 1:
      minStepsList[i] = 0
    else:
      ans1 = ans2 = ans3 = sys.maxsize
      if i%2 == 0:
        ans1 = minStepsList[i//2]
      if i%3 == 0:
        ans2 = minStepsList[i//3]
      ans3 = minStepsList[i - 1]
      minStepsList[i] = 1 + min(ans1, ans2, ans3)
    
  return minStepsList[n]

print(minStepsTo1I(20))

import math
def r_minSquaresOfN(n):
  if n <= 1:
    return 1
  root = int(math.sqrt(n))
  print(root)
  for i in range(2, root):
    ans = 1 + r_minSquaresOfN(n - i**2)


