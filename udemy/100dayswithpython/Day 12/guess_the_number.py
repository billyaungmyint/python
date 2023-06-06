#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)

number_to_guess = random.randint(1,100)
player_guess = 0
player_lives = 10
guessed_correctly = False




while guessed_correctly == False:
    player_guess = int(input("Pls guess a number between 1 and 100 : "))
    if player_guess == number_to_guess:
        print("You have guessed correctly!")
        guessed_correctly = True
    elif player_guess < number_to_guess:
        player_lives -= 1
        print("You have guessed too low. Pls try again")
        print(f"You have {player_lives} remaining")
        guessed_correctly = False
    else :
        player_lives -= 1
        print("You have guessed too high. Pls try again")
        print(f"You have {player_lives} remaining")
        guessed_correctly = False