# Write a function called sum_even_odds() that takes in a single parameter, nums. The function returns a list where the first element is the sum of the even numbers in nums and the second element is the sum of the odd numbers in nums.

def sum_even_odds(nums):
  even_count = 0
  odd_count = 0
  for x in nums:
    if x % 2 == 0: #even
      even_count += x
    else: #odd
      odd_count += x
  # print([even_count, odd_count])
  # print()
  return [even_count, odd_count]
# Test your program below
print(sum_even_odds([4, 9, 6, 0, 8, 3, 2])) 
print(sum_even_odds([2, 2, 2]))
print(sum_even_odds([]))
print()

def print_backwards(lst):
  """Alt Solution
  Using splicing [::-1] using loop + return
  """
  new_list = []
  #print("Original:", lst)
  while len(lst) != 0:
    x = lst.pop()
    new_list.append(x)
  #print("Backwards:", new_list)
  return new_list
  
print(print_backwards([1, 2, 3]))
print(print_backwards(["peach", "orange", "apple", "banana"]))
print()