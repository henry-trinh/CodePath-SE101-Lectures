import time

def find_match1(list1, list2): #Slower
  for i1, item1 in enumerate(list1):
    for i2, item2 in enumerate(list2):
      if i1 == i2 and item1 == item2:
        return i1
  return None

def find_match2(list1, list2): #Faster
  for i, item1 in enumerate(list1):
    item2 = list2[i]
    if item1 == item2:
      return i
  return None

# Verify Test Cases
list1 = [1,2,3]
list2 = [3,2,1]

start = time.time()
print("Output for find_match1", find_match1(list1, list2))
end = time.time()
print("Time for find_match1", end-start)
print()

start = time.time()
print("Output for find_match2", find_match2(list1, list2))
end = time.time()
print("Time for find_match2", end-start)

# Big List Test Cases
print()
print("Test Cases with Big Lists\n")
list1 = list(range(1000))
list2 = list(range(1, 1001))

start = time.time()
print("Output for find_match1", find_match1(list1, list2))
end = time.time()
print("Time for find_match1", end-start)
print()

start = time.time()
print("Output for find_match2", find_match2(list1, list2))
end = time.time()
print("Time for find_match2", end-start)