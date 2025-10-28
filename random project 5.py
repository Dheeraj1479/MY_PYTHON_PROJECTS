people = int(input("Enter how many people are going in the theme park: "))
total = people * 15

if people >= 6:
    total -= 5

print(f"Your total is £{total}")