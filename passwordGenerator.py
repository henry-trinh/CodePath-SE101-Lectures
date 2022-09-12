#First four are alphabetical random values
#Last four are digital random values

import string
import random

letter = random.choice(string.ascii_letters) #randomly uppercase or lowercase, adding additional security

def random_password(char):
  final_string = "".join(random.choice(string.ascii_letters) for i in range(char))
  str(final_string)

  final_num = "".join(random.choice(string.digits) for x in range(char))  
  str(final_num)

  print(final_string + final_num) #concatenates

#random_letter(4)

def revised_password(char, desired_len):
  password = ""
  
  first_letter = str(random.choice(string.ascii_letters))
  last_digit = str(random.choice(string.digits))

  password.append(first_letter)
  print(password)

  remaining = desired_len - 2

  while remaining != 0:
    for i in remaining:
      

  

  
  


