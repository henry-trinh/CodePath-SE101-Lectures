def has_222(nums):
  for i in range(len(nums) - 2): #subtract 2 to be in range if 222 occurs at end of list
    print("i: ", i, "       i+1: ", i+1, "       i+2: ", i+2)
    print("nums[i]: ", nums[i], " nums[i+1]: ", nums[i+1], " nums[i+2]: ", nums[i+2])
    if nums[i] == 2 and nums[i + 1] == 2 and nums[i + 2] == 2:
      return True
  return False

print(has_222([1]))