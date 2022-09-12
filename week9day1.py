"""PROBLEM 1"""
# Given a list lst with 0s and 1s, find the count of the maximum number of consecutive 1s present in the list.

# Example

# Input: lst = [1, 1, 1, 0, 1]
# Output: 3

# Input: lst = [0, 1, 0, 1, 1, 0, 0]
# Output: 2

def consecutives_ones(lst):
  ptr1 = 0
  current_max = 0
  max = 0
  while ptr1 < len(lst):
    if lst[ptr1] == 1:
      current_max += 1
      if current_max > max:
        max = current_max
    else:
      current_max = 0
    ptr1 += 1
  return max
  
assert(consecutives_ones([1, 1, 1, 0, 1]) == 3) #3
assert(consecutives_ones([0, 1, 0, 1, 1, 0, 0]) == 2) #2

print(consecutives_ones([1, 1, 1, 0, 1])) #3
print(consecutives_ones([0, 1, 0, 1, 1, 0, 0])) #2
print()

"""CODEPATH SUGGESTED SOLUTION

def consecutive_ones(lst):
    max_count = 0
    curr_count = 0
    for num in lst:
        if num == 1:
            curr_count += 1
        else:
            curr_count = 0

        if curr_count > max_count:
            max_count = curr_count

    return max_count

"""

"""PROBLEM 2""" #Get and In Methods for Dictionaries/HashMaps -> No difference in efficiency

capitals = {"USA": "Washington DC", "Canada": "Ottawa"}
capitals["Mexico"] = "Mexico City"

# If the country is in the dictionary capital, print the associated capital. Otherwise, print "Not Found"

country = "USA"
# Add code below using the get method
print(capitals.get(country, "Not Found"))

country = "France"
# Add code below using the in method
if country in capitals:
  print(capitals[country])
else:
  print("Not Found")
  
print()

"""PROBLEM 3"""

# Write the function total_inventory, which takes two inventory dictionaries and a key and gives the total count of the item from both inventory lists. 

# Make sure it doesn’t produce an error if the item isn’t in the inventory lists (in this case assume the value is 0).

# Example

# Input
# -----
# inventory_0 = {"bananas": 2}
# inventory_1 = {"bananas": 5, "apples": 3}
# item = "bananas"

# Output
# ------
# 7

def total_inventory(inventory_0, inventory_1, item):
  if item in inventory_0 or inventory_1:
    return int(inventory_0.get(item, 0) + inventory_1.get(item, 0))
  if item not in inventory_0 or inventory_1:
    return 0
print(total_inventory({"bananas": 2}, {"bananas": 5, "apples": 3}, "bananas"))

print()

"""PROBLEM 4"""
# Write the function translate which takes a list of words in one language and a translation dictionary, and uses the translation dictionary to return a list of words in the second language.

# Example:

# Input
# -----
# words = ["hello", "world"]
# dictionary = {"hello": "hola", "world": "mundo"}

# Output
# ------
# ["hola", "mundo"]

def translate(words, dictionary):
  #for word in words:
  #return [dictionary.get(word) for word in words if word in dictionary]
  #CODEPATH SOLUTION: OPTIMIZED FOR STORAGE
  for i in range

print(translate(["hello", "world"], {"hello": "hola", "world": "mundo"}))

print()


"""PROBLEM 5: BONUS (ASKED BY GOOGLE)""" 
# Given two strings which are of lengths n and n+1. The second string contains all the characters of the first string, but there is one extra character. Find the extra character in the second string. Using a dictionary! IF OUT OF TIME: SOLUTION FOUND HERE: https://replit.com/@rxlknl/Extra-Character?v=1#solution.py

# Input
# -----
# strA = "abcd"
# strB = "cbdae"

# Output
# ------
# "e"

def extra_char(strA, strB):
  for letter in strA:
    print(strB.get(letter))
print(extra_char("abcd", "cbdae")
  