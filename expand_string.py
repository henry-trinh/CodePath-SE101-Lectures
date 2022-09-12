# Take in a list of strings
# Concatenate strings
# Repeat the concatenated string 5x 
# Capitalize the result 

def expand_string(listOfStrings):
  newString = "".join(listOfStrings)
  return newString.upper() * 5
 
print(expand_string(['x', 'y', 'z']))