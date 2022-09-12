"""
Goal:  Given an list lst and an integer w, find the maximum for each and every contiguous (connected) sublist of size w.

Input:     lst = [1, 2, 3, 1, 4, 5]; w = 3
Output:  "3 3 4 5"  
"""

# def sliding_windows(lst, w):
#   ptr1 = 0
#   ptr2 = ptr1 + int(w) # + 1, no due to splicing exclusivity
#   solution = ""
  
#   while ptr2 <= len(lst):
#     parse_solution = max(lst[ptr1:ptr2])
#     solution += str(parse_solution) + " "
#     ptr1 += 1
#     ptr2 += 1
#   print(solution)

""" PRIOR TO DEBUGGING
def sliding_windows(lst, w):
  ptr1 = 0
  ptr2 = ptr1 + int(w) # + 1, no due to splicing exclusivity
  solution = ""
  
  while ptr2 < len(lst):
    parse_solution = max(lst[ptr1:ptr2])
    solution += str(parse_solution)
    print(solution)
    ptr1 += 1
    ptr2 += 1
  
print(sliding_windows([1, 2, 3, 1, 4, 5], 3))
"""

def isPairSum(lst, x):
  for i in range(0, len(lst)):
    for j in range(i + 1, len(lst)):
      if lst[i] + lst[j] == x:
        return True
  return False

lst = [10, 20, 35, 50, 75, 80]
print(isPairSum(lst, 70))

def isRepeat(lst):
  # Remove duplicates in a sorted list
  # Since sorted, duplicates always adjacent to proceeding value in lst

  ptr1 = 0
  ptr2 = 1

  while ptr2 < len(lst):
    while lst[ptr2] == lst[ptr1]:
      lst.pop(lst[ptr2])
    ptr1 += 1
    ptr2 += 1 
  return lst

print(isRepeat([1, 2, 2, 3, 3, 4, 5]))
