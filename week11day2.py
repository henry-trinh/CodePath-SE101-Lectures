def fibonacci(index): #RECURSIVE 1
  
  # if index == 0: #base case
  #   return 0
  # if index == 1:
  #   return 1
  if index <= 1:
    return index
  else: #recursive case
    return fibonacci(index - 1) + fibonacci(index - 2)

def fibonacci_iterate(index): #ITERATIVE 1
  res = 0
  for num in range(0, index + 1):
    res += num
  return res

print(fibonacci(10)) #55
print(fibonacci_iterate(10)) #55

def palindrome(str):
  if len(str) <= 1:
    return True
  else:
    if str[0] == str[-1]:
      return palindrome(str[1:-1])
    else:
      return False

def palindrome_iterative(str):
  ptr1 = 0
  ptr2 = len(str) - 1

  while ptr2 > ptr1:
    if str[ptr1] != str[ptr2]:
      return False
    ptr1 += 1
    ptr2 -= 1
  return True

print(palindrome("racecar"))
print(palindrome_iterative("racecar"))
