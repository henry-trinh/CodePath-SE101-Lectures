# Problem: Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

# A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] and so do the numbers [2,4]. 

# Note that a single number in an array and the array itself are both valid subsequences of the array.

# True case
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence_1 = [1, 6, -1, 10]

# True case
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence_2 = [-1]

# False case
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence_3 = [10, -1]

# True case
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence_1 = [1, 6, -1, 10]

#arrayTot = len(sequence_1)
def subsequence(array, sequence):
  count = 0
  arrayTot = len(sequence)
  print(arrayTot)
  
  for element in array:
    print(element)
    if element in sequence:
      count += 1
      print(count)
    else:
      array.remove(element)
      print(array)
  print(count)
  if count == arrayTot:
    #new condition for sort
    return True
  else:
    return False

subsequence(array, sequence_3)