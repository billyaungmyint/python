'''create a random number between 1 and 10'''
import random
secret_num = random.randint(1, 10)
print(secret_num)

'''ask the user for a guess'''
guess = int(input("Guess a number between 1 and 10: "))
'''keep asking until they get it right'''
while guess != secret_num:
    guess = int(input("Guess again: "))
print("You got it! My number was {}".format(secret_num))
