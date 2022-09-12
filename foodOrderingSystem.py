"""
1. Print a numbered list of the menu items.
2. Continuously ask the user for the item number they want to add to their order. 
3. Stop prompting the user to enter item numbers if user enters Done.
4. Print a goodbye message and the items in the user’s order. 
"""
menu = ["Iced Coffee", "Blonde Roast", "Matcha Latte", 
        "Cold Brew", "Caramel Macchiato", "Pumpkin Spice Latte", "Peppermint Mocha", "Iced Green Lemonade", 
        "Mango Dragonfruit Refresher", "Iced Dirty Chai Latte"]

print("-- ☕️ STARBUCKS MENU ☕️ -- ")
for ind, val in enumerate(menu):
  print(ind+1, val)

order = []

initial = input("\nWould you like anything to order? (1-10) ")
initial = int(initial)
menu_item = menu[initial - 1]
order.append(menu_item)

while True:
  newOrder = input("\nWould you like anything else? ")
  if str(newOrder.title()) == "Done":
    break
  menu_item = menu[int(newOrder) - 1]
  order.append(menu_item)

print("\nThanks! Here is your complete order: ")
for element in order:
  print(element)

#Future work: Code has if/else statements based on input type

  