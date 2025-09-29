import random

words_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(words_list)
print(chosen_word)

game = False
correct = []

placeholder = ""

for l in chosen_word:
    placeholder += '_'
print(placeholder)
lives = 6
while not game:

    guess = input("Guess a letter: ")
    guess = guess.lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct.append(guess)
        elif letter in correct:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game = True
        print("You win!")
    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left.")
        if lives == 0:
            game = True
            print("You lose")


