"""A number-guessing game."""
# Put your code here

from random import randint

print("Hello") # greet player

name = input("What's your name: ") # get player name

play_again = True

def repeat_game():
    response = input("Play again? y/n: ")
    if response.lower() == 'y':
        return True
    return False
    
def play_guessing_game():
    num = randint(1,101) # choose random number between 1 and 100
    guess_count = 0

    while True:
        guess = int(input("Guess: "))
        guess_count += 1
        if guess > num: # guess is too high
            print("Try a lower number")
        elif guess < num: # guess is too low
            print("Try a higher number")
        else:
        # congratulate player
            print(f"Congratulations, {name}! You guessed it in {guess_count} guesses!")
            return # end program

while play_again is True:
    play_guessing_game()
    play_again = repeat_game()

