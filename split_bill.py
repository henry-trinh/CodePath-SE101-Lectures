# Prompt the user for the cost of the bill
bill_cost = input("What was the total cost of your bill? ")

# Prompt the user for the number of people in the party
party_total = input("\nHow many people were in your party? ")

# Hint: You might need to strip the '$' from the cost of the bill string
if "$" in bill_cost:
  bill_cost = bill_cost[1:]

# Calculate the split bill
split_bill = float(bill_cost) / int(party_total)

# Print what each person owes 
print("\nEach person owes $" + str(split_bill))