import random 
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#chosen_word = word_list[random.randint(0,len(word_list) - 1)]
chosen_word = random.choice(word_list)
#print(chosen_word)
                

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("\nPls guess a letter : \n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
counter = 0

# while counter < len(chosen_word):
#     if guess == chosen_word[counter]:
#         print("Right")
#         counter += 1
#     else:
#         print("Wrong")
#         counter += 1 

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")