"""A number-guessing game."""
# Put your code here

from random import randint

print("Hello") # greet player

name = input("What's your name: ") # get player name
num = randint(1,101) # choose random number between 1 and 100

while True:
    guess = int(input("Guess: "))
    if guess > num: # guess is too high
        print("Try a lower number")
    elif guess < num: # guess is too low
        print("Try a higher number")
    else:
    # congratulate player
        print(f"Congratulations, {name}! You guessed it!")
        break # end program

