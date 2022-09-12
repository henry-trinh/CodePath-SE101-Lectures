"""Given a string str1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters"""

def stringParse(str1):
  digits = "1234567890"
  sum = 0
  count = 0
  for char in str1:
    if char not in digits:
      continue
    else: #is a digit
      sum += int(char)
      count += 1
  average = sum/count
  return sum, average

#Test Cases
print(stringParse("hwhtwhw3424h3532"))

"""Challenge: Return length of the longest consecutive substring of numeric characters"""

def longestConsecutiveSubstring(str1):
  current_longest = 0
  longest = 0
  digits = "1234567890" #could use isDigit() method
  
  for char in str1:
    if char not in digits:
      if current_longest > longest:
        longest = current_longest
      current_longest = 0
    else:
      current_longest += 1
      if current_longest > longest:
        longest = current_longest
      
  return longest

#Test Cases
print(longestConsecutiveSubstring("hwhtwhw42334h325334435xsdfses3234235235233xx2321"))


  