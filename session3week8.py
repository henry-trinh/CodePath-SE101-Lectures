''' PROBLEM 4
Write a function `remove_members` that returns an updated `member_list` that contains only students who have graduated and are in good standing.

A student is considered graduated if their graduation year is equal to or less than year.
'''
def remove_members(member_list, year):
  sol = []
  for i in range(len(member_list)):
    for j in range(len(member_list[0])):
      if member_list[i][1] <= year and member_list[i][2] == True:
        sol.append(member_list[i][j])
  return sol

# Test Cases
member_list = [["Jane Smith", 2019, False],
              ["Steve Fox", 2018, True ],
              ["Michael Xin", 2017, False],
              ["Maria Garcia", 2020, True]]

year = 2018

print("Input \nmember_list = ", member_list, "\nyear = ", year)
print("Output: ", remove_members(member_list, year))

member_list = [["Jane Smith", 2019, False],
              ["Steve Fox", 2018, True ],
              ["Michael Xin", 2017, False],
              ["Maria Garcia", 2020, True]]

year = 2020

print("\nInput \nmember_list = ", member_list, "\nyear = ", year)
print("Output: ", remove_members(member_list, year))

member_list = []
year = 2022

print("\nInput \nmember_list = ", member_list, "\nyear = ", year)
print("Output: ", remove_members(member_list, year))

""" PROBLEM 5
Write a function max_difference that takes in an integer list and returns the maximum difference between the elements in the list such that the element values are increasing. Where nums[i] < nums[j] and i < j.

Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].
"""
def max_difference(nums):
  print()
  maxDiff = -1
  curr_minNum = nums[0]
  for i in range(len(nums)):
    maxDiff = max(maxDiff, nums[i] - curr_minNum)
    curr_minNum = min(curr_minNum, nums[i])
  
  if maxDiff != 0:
    return maxDiff
  else:
    return -1

# Test Cases
nums = [7, 1, 5, 4]
print("Input: ", nums)
print("Output: ", max_difference(nums))

nums = [9, 4, 3, 2]
print("\nInput: ", nums)
print("Output: ", max_difference(nums))

nums = [1, 5, 2, 10]
print("\nInput: ", nums)
print("Output: ", max_difference(nums))

"""PROBLEM 6
Write a function reverse_columns that takes in an 2D list matrix and reverse the order of the columns.

Input: nums =   [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]]
Output: nums =  [[2, 1, 0],
                [5, 4, 3],
                [8, 7, 6]]

Input: nums =   [[0, 1, 1, 1, 2],
                [3, 4, 7, -1, 2],
                [6, 6, 8, 5, 4]]
Output: nums =  [[2, 1, 1, 1, 0],
                [2, -1, 7, 4, 3],
                [4, 5, 8, 6, 6]]
"""

def reverse_columns(matrix):
  print()
  for col in range(0, len(matrix[0])):
    for row in range(0, len(matrix)):
      return matrix[row]
      

# Test Cases
matrix = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]

print("Input \n", matrix)
print("Output \n", reverse_columns(matrix))

matrix = [[0, 1, 1, 1, 2],
         [3, 4, 7, -1, 2],
         [6, 6, 8, 5, 4]]

print("\nInput \n", matrix)
print("Output \n", reverse_columns(matrix))