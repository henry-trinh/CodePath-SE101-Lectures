# Write a function `happyNewYear` that takes in a single parameter, `year`. 
# If it is a new **millennium**, the function should print `“Happy New Millenium!”`. If it is a new **decade**, the function should print `“Happy New Decade!”`, otherwise it should print `“Happy New Year!”`. 

def happyNewYear(year):
  if year % 1000 == 0:
    print("Happy New Millenium")
  elif year % 10 == 0:
    print("Happy New Decade!")
  else:
    print("Happy New Year!")

# Write a function called `isAFactor` that when given two integer parameters , `num1` and `num2`, returns `True` if `num1` is a factor of `num2` and `False` otherwise.

# Try writing the function from scratch. Use the naming conventions as specified in the problem description above!

def isAFactor(num1, num2):
  if num1 % num2 == 0 or num2 % num1 ==0:
    return True
  else:
    return False

# These lines of code are used to test our function.
# Test Case #1: should return True
print(isAFactor(10,70))

# Test Case #2: should return False
print(isAFactor(3,70))

#Test Case #3: should return True
print(isAFactor(1,7))

#Add your own testcase below!

# These lines of code are used to test our function.
# Test Case #1: should print Happy New Millenium!
happyNewYear(2000)

# Test Case #2: should print Happy New Decade!
happyNewYear(2010)

#Test Case #3: should print Happy New Year!
happyNewYear (2001)
