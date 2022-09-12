"""
Given a 2D list of characters lst and a target string word. Count the number of occurrences of the given word in the 2D list. Words can be found in four directions: horizontally left, horizontally right, vertically up and vertically down.

Input: 
  word = “cab”
  lst = [['c','a','b','z','c'],
        ['r','a','r','y','a'],
        ['b','w','o','w','b'],
        ['a','x','d','a','e'],
        ['c','o','b','a','c']]

Output: 4
"""

def word_search(lst, word): # start at origin lst[0][0]
  #parse_word = ""
  count = 0
  lw = len(word)
  for row in range(0, len(lst)):
    for col in range(0, len(lst[row])): 
      #Horizontal, Right AND Left
      if lst[row][col] == word[0]: #first letter match
        #print("test")
        #currently comparing str to list --> use join to convert 
        x = "".join(lst[row][col:col + lw])
        str(x)
        #print(len(x))
        print(x)
        #print(word)
        #print(word[::-1])
        if x == word or x == word[::-1]:
          #print("test2")
          count += 1
  print(count)
 
          
    #Vertical, Left
  
    #Vertical Right
            
lst = [['c','a','b','z','c'],
      ['r','a','r','y','a'],
      ['b','w','o','w','b'],
      ['a','x','d','a','e'],
      ['c','o','b','a','c']]
word = "cab"
  
word_search(lst, word)

"""CODEPATH SOLUTION
def word_search(grid, word):
  if len(word)>len(grid): return 0
    
  count = 0
  
  #check horizontally
  for row in range(len(grid)):
    p1 = 0 
    p2 = len(word)
    
    while p2 < len(grid): 
      w1 = ''.join(grid[row][p1:p2])
      w2 = ''.join(grid[row][p1:p2:-1])
      if w1 == word: 
        count += 1 
        print("Row:", row, " Col:", p1)
      if w2 == word: 
        count += 1 
        print("Row:", row, "Col:", p1)
      p1 += 1
      p2 += 1

  #check vertically
  for c in range(len(grid[0])): 
    for r in range(len(grid)-len(word)+1):
      w1 = '' 
      w2 = ''
      for l in range(r, r+len(word)):
        w1 += grid[l][c] 
        w2 += grid[-l-1][c] 
      if w1==word: 
        count += 1 
        print("vertical, ","Row:", r, " Col:", c)
      if w2==word: 
        count += 1 
        print("vertical, ","Row:", r, " Col:", c)

  return count


lst = [["c", "a", "b", "z", "c"], 
       ["r", "a", "r", "y", "a"], 
       ["b", "w", "o", "w", "b"], 
       ["a", "x", "d", "a", "e"], 
       ["c", "o", "b", "a", "c"]]
word = "cab"

print(word_search(lst, word))
"""