print("Welcome to the Treasure Island.\nYour mission is to find the treasure.\nYou're at a cross road. Where do you want to go?")
choice = input("Type 'left' or 'right'. ")
if choice == 'right':
    print("You fell into a hole. Game Over")
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input("Type 'wait' to wait for the boat. Type 'swim' to swim across")
    if choice2 == 'swim':
        print("You get attacked by an angry trout. Game Over ")
    else:
        print("You arrive at the island unharmed.There is a house with 3 doors.")
        choice3 = input("One red, one yellow and one blue. Which colour do you choose?")
        if choice3 == 'red':
            print("It's a room full of fire. Game Over.")
        elif choice3 == 'yellow':
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")