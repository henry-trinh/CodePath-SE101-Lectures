color = input("Color of Animal? ")
height = input("Height of Animal (in feet)? ")

if color == "yellow" or color == "Yellow":
  if int(height) == 10:
    print("Your animal is a Giraffe!")
  else:
    print("Your animal is a Tiger!")
else:
  if int(height) < 10:
    print("Your animal is a Monkey!")
  else:
    print("Your animal is an Elephant!")