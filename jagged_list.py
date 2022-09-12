"""
Goal: A jagged list is a 2D list where the sublist are of different lengths. Write a function called is_jagged() that takes a single parameter, a 2D list called lst. If the 2D list is jagged, return True. Otherwise, False.
"""

def is_jagged(lst):
  standard = lst[0] # Not jagged if all sublists are the same length as the first
  for sublist in lst:
    if len(sublist) != len(standard):
      return True #Jagged
  return False

x =  [[1,2,3], [4,5,6,7], [8, 9, 10]] #True
y = [[1,2,3], [4,5,6], [7,8, 9]] #False

print(is_jagged(x))
print(is_jagged(y))
assert(is_jagged(x) == True)
assert(is_jagged(y) == False)
