import random
secret_number = random.randint(1, 100)
print(secret_number)

'''
1. Link/Import the random Python library
2. Change the secret_number variable to the output of a randint() function. Let’s choose a random number from 1 to 100 inclusively. 
3. Print the secret_number at start so we know if our program is working correctly. 

Now test it out!
'''

guess = int(input("Guess a number! "))
# Define the function `guess_number` here
def guess_number(guess):
  if guess > secret_number:
    print("Your guess is higher than the correct number. Try again.")
  elif guess < secret_number:
    print("Your guess is lower than the correct number. Try again!")
  else:
    print("Guess is correct")

# Add calls to the function below
guess_number(guess)