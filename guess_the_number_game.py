import random

number = random.randint(1, 100)
is_guess_number = False
print("Welcome to Number Guessing Game!")
print("Guess the number between 1 and 100.")
guesses = int(input("How many guesses you need to guess? : "))
for guess in range(guesses):
    print(f"You have {guesses} guesses left")
    guess = int(input("Guess a number : "))
    if guess == number:
        is_guess_number = True
        print("You guessed the number correctly!")
        break
    elif guess < number:
        print("Wrong Guess!! Try High number.")
    elif guess > number:
        print("Wrong Guess!! Try Low number.")
    else:
        print("Invalid Entry!!")
    guesses -= 1
if is_guess_number == False:
    print(f"The secret number was {number}. You are out of guesses")
    print("Better luck next time!!")
print("Game Over!!")