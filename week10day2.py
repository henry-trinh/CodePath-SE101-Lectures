import time

"""PSET 1
# Create a list with 100000 items using the range() method
mylist = range(100001)
mylist = list(mylist)

# Printing the element at index 100000
print("Executing print element at index 100000")
start = time.time()
mylist[100000]
end = time.time()
print(end - start)

# Popping the last element off of the list
print("\n Popping the last element off the list")
start = time.time()
mylist.pop()
end = time.time()
print(end - start)

# Popping the first element off of the list
print("\n Popping the first element off of the list")
start = time.time()
mylist.pop(0)
end = time.time()
print(end - start)

# Appending an element to the end of the list
print("\n Appending an element to the end of the list")
start = time.time()
mylist.append(100001)
end = time.time()
print(end - start)

# Inserting an element at index 0
print("\n Inserting an element at index 0")
start = time.time()
mylist.insert(0, 100001)
end = time.time()
print(end - start)

# Inserting/Popping at end of List is easier O(1) compared to at beginning of List O(n)
"""

"""PSET 2

print("/nDICTIONARY METHODS TIME")
# Create a list with 100000 items using the range() method
mylist = list(range(100000))

# Create a dictionary with 100000 items using the range() method
mydict = {}
for i in range(100000):
     mydict[i] = i

# Access the element at key 10000
print("\n Access the element at key 10000")
start = time.time()
mydict.get(10000-1)
end = time.time()
print(end-start)

# Add a new key-value pair to the dictionary
print("\n Add a new key-value pair to the dictionary")
start = time.time()
mydict[10000] = 1
end = time.time()
print(end-start)

# Increment the value at key 10 by 1
print("\n Increment the value at key 10 by 1")
start = time.time()
mydict[10 - 1] += 1
end = time.time()
print(end-start)

# Delete key 10000
print("\n Delete key 10000")
start = time.time()
mydict.pop(10000 - 1)
end = time.time()
print(end-start)

# Check if the key 10 is in the dictionary
print("\n Check if the key 10 is in the dictionary")
start = time.time()
check = False
if mydict[10] in mydict:
  check = True
end = time.time()
print(end-start)

# Check if the key -10 is in the dictionary
print("\n Check if the key -10 is in the dictionary")
start = time.time()
check2 = False
if -10 in mydict:
  check2 = True
end = time.time()
print(end-start)

# Pop the first item off of the list
print("\n Pop the first item off of the list")
start = time.time()
mylist.pop(0)
end = time.time()
print(end-start)

# Pop the last item off of the list
print("\n Pop the last item off of the list")
start = time.time()
mylist.pop()
end = time.time()
print(end-start)
"""

"""PSET 3: PRACTICE WITH DICTIONARIES"""
print("SUM TO ZERO")
# SUM TO ZERO
def sum_to_zero(my_list):
  '''
    Find two elements from my_list which sum to zero.
    Return a tuple of the two elements if they exist and None otherwise.
  '''
  # WITHOUT DICTIONARIES
    # for item1 in my_list:
    #     for item2 in my_list:
    #         if item1 + item2 == 0:
    #             return item1, item2
    # return None
  #We know we will sum, so we need to add pos num PLUS neg num counterpart. 
  
  dict = {}
  for num in my_list:
    dict[num] = num
  for num in my_list:
    if dict[-num] in my_list:
      return num, -num
  return None
  
# Test Cases
my_list = [4, 5, -7, -3, 8, -4]
start_time = time.time()
result = sum_to_zero(my_list)
end_time = time.time()
total_time = end_time - start_time
print("Input:", my_list)
print("Output:", sum_to_zero(my_list))
print("Time", total_time)

# MOST COMMON ITEM
print("\nMOST COMMON ITEM")
def most_common_item(my_list):
  '''
  Return the item that occurs the most frequently in my_list.
  '''
  # most_common_item = None
  # most_common_count = None
  # for item in my_list:
  #     count = 0
  #     for item2 in my_list:
  #         if item2 == item:
  #             count += 1
  #     if most_common_count is None or count > most_common_count:
  #         most_common_item = item
  #         most_common_count = count
  # return most_common_item
  dict = {}
  for item in my_list:
    if item in dict:
      dict[item] += 1
    else:
      dict[item] = 1
  #return max(dict, key = dict.get)
  
# Test Cases
my_list = [1, 2, 3, 3, 4, 2, 2, 1, 3, 2]
start_time = time.time()
result = most_common_item(my_list)
end_time = time.time()
total_time = end_time - start_time
print("Input:", my_list)
print("Output:", most_common_item(my_list))
print("Time", total_time)

# HAS DUPLICATES