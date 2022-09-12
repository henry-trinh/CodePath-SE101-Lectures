import random
import math

def snake_eyes():
  rolls = 0
  doubles = 0
  dice1_sum = 0
  dice2_sum = 0
  
  while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    dice1_sum += dice1
    dice2_sum += dice2
    rolls += 1

    if dice1 == dice2:
      doubles += 1
      
    print("Roll", rolls, "-> Die 1:", dice1, "and Die 2:", dice2)

    if dice1 == 1 and dice2 == 1:
      break
      
  d1_avg = dice1_sum / rolls
  d1_avg = round(d1_avg, 2)
  d2_avg = dice2_sum / rolls
  d2_avg = round(d2_avg, 2)

  print()
  print("You got Snake Eyes!\n")
  print("Total Number of Rolls:", rolls)
  print("Total Number of Doubles:", doubles)
  print("Average Roll for Die #1:", d1_avg)
  print("Average Roll for Die #2:", d2_avg)
  #math.round()
  
snake_eyes()