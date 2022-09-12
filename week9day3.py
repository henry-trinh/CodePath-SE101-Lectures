"""PROBLEM 5

Write the function letter_count(), which takes a word list and returns a dictionary which has the letters as keys and the values the number of times each letter appears in the word list.

"""

def letter_count(word_list):
  output = {}
  for word in word_list:
    for letter in word:
      if letter not in output:
        output[letter] = 1
      else: 
        output[letter] += 1
  return output
      

# Test Cases
word_list = ['car', 'bat', 'rat']
print("Input: ", word_list)
print("Output: ", letter_count(word_list)) # {'c': 1, 'a': 3, 'r': 2, 'b': 1, 't': 2}

word_list = ["the", "quick", "brown", "fox", "jumps", "over", "the", "big", "red", "dog"]
print("\nInput: ", word_list)
print("Output: ", letter_count(word_list)) # {}

"""PROBLEM 6

Write the function most_common_letters() which takes a dictionary with letters as keys and values as the count of that letter and returns the a list of the letters with the highest count. The list can have any number of letters in it depending on how many letters are tied for the highest count.

**Solved, but unoptimized (runs through dictionary twice)
"""

def most_common_letters(letter_counts):
  solution = []
  max_val = 0
  for letter in letter_counts:
    if letter_counts[letter] >= max_val:
      max_val = letter_counts[letter]
  for letter in letter_counts:
    if letter_counts[letter] == max_val:
      solution.append(letter)
  return solution
      
#Test Cases
letter_counts = {'c': 1, 'a': 3, 'r': 2, 't': 2, 'b': 1}
print("Input: ", letter_counts)
print("Output: ", most_common_letters(letter_counts)) # ['a']

letter_counts = {'c': 1, 'a': 3, 'r': 3, 't': 3, 'b': 1}
print("\nInput: ", letter_counts)
print("Output: ", most_common_letters(letter_counts)) # ['a', 'r', 't']

"""PROBLEM 7

Write the function count_by_state() which gives the count of people in a given state. It takes the following as input:

locations: a dictionary with names as keys and their city as the value.
states: a dictionary with cities as the keys and the state the city is in as the value.

CODEPATH SOLUTION:
  total = 0
  for name, city in locations.items():
    if states[city] == state:
      total += 1
  return total
"""
def count_by_state(locations, states, state):
  count = 0
  for key, value in states.copy().items(): #copy() to avoid "dictionary changed size during iteration" error
    if value != state:
      del states[key]
  # print("new states", states)
  # for value in locations.values():
  #   for key in states:
  #     if locations[key] == states[key]:
  for key in locations:
    if locations[key] in states:
        count += 1
  return count

# Test Cases
locations = {"Bob": "San Francisco", "Anna": "Los Angeles", "Charlie": "Detroit"}
states = {"San Francisco": "California", "Los Angeles": "California", "Ann Arbor": "Michigan", "Detroit": "Michigan"}

state = "California"
print("Input")
print("\tlocations = ", locations)
print("\tstates = ", states)
print("\tstate = ", state)
print("Output: ", count_by_state(locations, states, state)) #2

state = "Michigan"
print("\nInput")
print("\tlocations = ", locations)
print("\tstates = ", states)
print("\tstate = ", state)
print("Output: ", count_by_state(locations, states, state)) #1

state = "Texas"
print("\nInput")
print("\tlocations = ", locations)
print("\tstates = ", states)
print("\tstate = ", state)
print("Output: ", count_by_state(locations, states, state)) #0