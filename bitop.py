def conv_bin(num, bw=8):
  if num < 0:
    num += 2**bw
  return bin(num)[2:].zfill(8)

def conv_dec(num, bw=8):
  decnum = int(num, 2)
  if num[0] == "0":
    return decnum
  else:
    return decnum - 2**bw

def swap_num(num1, num2):
  num1 = num1 ^ num2
  num2 = num1 ^ num2 
  num1 = num1 ^ num2
  return num1, num2

print(conv_bin(-6))
print(conv_bin(-5))
print(conv_bin(-4))
print(conv_dec("00000101"))
print(conv_dec("11111011"))
print(swap_num(5, 11))

if (-5 & (1 << 1)):
  print("YES")
else:
  print("NO")
print(4 & 3)