fruits = ["banana", "apple", "orange", "pear", "grape", "pineapple"]

user_input = str(input("What word would you like to find? :"))
for i in fruits:
    if i == user_input:
        print("True")
    else:
        print("False")
