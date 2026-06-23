import random

print("Welcome to the game")

print("Enter rock, paper or scissor")

choices = ["rock", "paper", "scissor"]
guess = random.choice(choices)
user = input("enter your choice : ")

print("Your choice is:", user)
print("Computer choice is:", guess)

if user == guess:
    print("Try again!!")
elif (user == "rock" and guess == "scissor") or (user == "paper" and guess == "rock") or (user == "scissor" and guess == "paper") :
     print("You won!!")
else:
    print("You lost!!")
