# Problem
# -------
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
#  - Open brackets must be closed by the same type of brackets.
#  - Open brackets must be closed in the correct order.

# Examples
# --------
# Input: s = "()[]{}"
# Output: True

# Input: s = "(]"
# Output: False

#Input: s = "((((((((({{{{{[[[[{}]]]]}}}}})))))))))"

def is_balanced(s):
  """
  open = "([{"
  close = ")]}"
  parenthesis_count = 0
  brackets_count = 0
  curly_braces_count = 0
  # In our code, we want these counters to be 0 at the end of running the program. 
  for char in s:
    while s[char] in open:
      reciprocal =
  """
  """ Rachael's Answer
  def is_balanced(s):
    lst =  []
    open = {"(", "{", "["}
    closed = {")", "]", "}"}
    for char in s:
      if char in open:
        if char == "{":
          lst.append("}")
        elif char == "(":
          lst.append(")")
        else:
          lst.append("]")
      elif char in closed:
        if char == lst[-1]:
          lst.pop(-1)
    if len(lst) == 0:
      return True
    return False
  
  print(is_balanced("()[]{}"))
  print(is_balanced("([)]{}"))
  print(is_balanced("([)]{[}]"))
  """
  
  """Correct Solution"""
  brackets = []
  for i in s:
      if i in ['(', '[', '{']:
          brackets.append(i)
      
      else:  # i in [')', ']', '}']
          last_bracket = brackets.pop()
          if i == ')' and last_bracket != '(':
            return False
          elif i == ']' and last_bracket != '[':
            return False
          elif i == '}' and last_bracket != '{':
            return False

  if len(brackets) == 0:
      return True
  else:
      return False

assert is_balanced('(){}[]') == True
assert is_balanced('{]') == False
assert is_balanced('([)]') == False
assert is_balanced('(())()') == True
assert is_balanced('(') == False
  
        
        
    
  