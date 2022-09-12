"""
Write a function called distinct_substrings(), that takes one string argument s . The function returns the number of substrings of length three, where none of the characters in the substring are the same.
"""

def distinct_substrings(s): #Problem 5
  
  ptr1 = 0
  ptr2 = 2
  count = 0
  
  while ptr2 <= len(s) - 1:
    if s[ptr1] != s[ptr2] and s[ptr1] != s[ptr1 + 1] and s[ptr2 - 1] != s[ptr2]:
      count += 1
      print(s[ptr1:ptr2+1])
    ptr1 += 1
    ptr2 += 1
  return count
    

# Test Cases
s = "aababcabc"
print("Input: ", s)
print("Output: ", distinct_substrings(s))

s = "xyzzaz"
print("\nInput: ", s)
print("Output: ", distinct_substrings(s))

"""
Write a function called longest_substring() that takes in a single parameter, s. The function returns the first length of the longest substring without repeating characters.
"""

def longest_substring(s): #Problem 6
  ptr1 = 0
  ptr2 = 1
  count = 0 
  
  while ptr1 <= len(s) - 1:
    while s[ptr1] !=  s[ptr2]:
      count += 1
      print(s[ptr1:ptr2 + 1])
    ptr1 += 1
    ptr2 += 1
      
# Test Cases
s = "pppppp"
print("Input: ", s)
print("Output: ", longest_substring(s)) # 1

s = "aabdcefabcbb"
print("\nInput: ", s)
print("Output: ", longest_substring(s)) # 6