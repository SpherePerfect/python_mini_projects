number = 18

guesses = 1

print("Hint: The number is somewhere between 8 and 28")

while guesses<=9:
    entered_number = int(input("Guess the number:"))
    if entered_number < number:
        print("You entered a smaller number, try again:")
    elif entered_number>18:
        print("You entered a greater number, try again:")
    else:
        print("You won!")
        print("You used",number_of_guesses_used,"guesses")
        break
    guesses_left = 9 - guesses
    number_of_guesses_used = 9 - guesses_left
    print(guesses_left, "guesses left\n")
    guesses = guesses + 1

if (guesses > 9):
    print("Game Over")


