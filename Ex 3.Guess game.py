n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times:")
while (number_of_guesses<=9):
    guess_number = int (input("Guess the number:\n"))
    if guess_number<18:
        print("you enter lesser number please enter greater number.\n")
    elif guess_number>18:
        print("you enter higher number please enter smaller number.\n")
    else:
        print("you won.\n")
        print(number_of_guesses,"no. of guesess he took finish.")
        break
    print(9 - number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses +1

if (number_of_guesses>9):
    print("game over")