total_bill = float(input("Enter the total bill:"))

true = bool(True)
while true:
    person_bill = float(input("Enter how much your paying for the bill:"))
    total_bill -= person_bill
    if total_bill > 0:
        print(f"Your bill is:{total_bill}")
    elif total_bill == 0:
        print("Bill paid")
        true = bool(False)
    else:
        amount_left = total_bill - 0
        print("Tip is", abs(amount_left))
        true = bool(False)

