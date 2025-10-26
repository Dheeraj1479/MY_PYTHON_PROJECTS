sweetid = input("Enter SweetID: ")
sweetname = str(input("Enter SweetName: "))
sweetname = sweetname[0:2]
brand = str(input("Enter Brand: "))
brand = brand[0]

code = sweetid + sweetname + brand
print(f"Your stock code is {code}")

