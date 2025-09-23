print("Welcome to the tip calculator!\nWhat was the total bill? $")
bill = float(input())
print("How much tip would you like to give? 10, 12, or 15?")
tip = int(input())
tipaspercent = tip / 100
print("How many people to split the bill?")
people = int(input())

tipthing = bill * tipaspercent
total = (bill + tipthing) / people
print("Each person should pay: $" + str(total))