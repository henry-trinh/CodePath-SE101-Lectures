""" 
Goal: Using a 2D list, create a booking system for a movie theatre consists of 40 seats, organized in 5 rows of 8 seats. If a seat is booked, its correspond cell in the 2D list has a value of 1. If empty,  it has a value of 0.
"""

print("* * * 🎟  Ticket Purchase Center 🎟 * * * ")
print("1️⃣: Book a single seat")
print("2️⃣: Book multiple seats in a row")
print("3️⃣: Book a backrow seat")
print("4️⃣: Exit\n")

# First create your 2d list representation 8 seats, 5 rows 
full_list = [[0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0]]
print(full_list)

# Go through each instruction

def movie_purchase(menu_input):
  menu_input = input("\nChoose a Menu Option: ")
  valid = "1234"
  while True:
    if menu_input not in valid:
      print("Oops! We couldn't understand that. Please try again.")
    if int(menu_input) == 1:
      row = input("\nWhat row would you like to sit in? ")
      col = input("What column would you like to sit in? ")
      print("\nExcellent choice! We'll book it right now.")
      full_list[int(row)][int(col)] = 1
      print(full_list)
    if int(menu_input) == 2:
      pass
    if int(menu_input) == 3:
      pass
    if int(menu_input) == 4:
      print("\nThank you for booking with us!")
      break