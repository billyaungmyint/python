# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


# print(chooseWord(wordlist))
# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    return all(x in lettersGuessed for x in secretWord)
    # for a in secretWord:
    #     if a not in lettersGuessed:
    #         return False
    # return True


# print(isWordGuessed(secretWord, lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return ''.join([i if i in lettersGuessed else '_ ' for i in secretWord])
    # ans = []
    # for a in secretWord:
    #     if a not in lettersGuessed:
    #         ans.append('_')
    #     else :
    #         ans.append(a)
    #
    # return ''.join(ans)


# print(getGuessedWord(secretWord, lettersGuessed))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    return ''.join([i for i in string.ascii_lowercase if i not in lettersGuessed])
    # availableLetters = []
    # for x in string.ascii_lowercase :
    #     if x not in lettersGuessed :
    #         availableLetters.append(x)
    #
    # return ''.join(availableLetters)


# print(getAvailableLetters(lettersGuessed))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    oldGuessList = []
    lettersGuessed = []
    i = 8
    while i > -1:
        print('-------------')
        print('You have', i, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        lettersGuessed.append(guess)
        if guess in secretWord and guess not in oldGuessList:
            print('Good Guess:', getGuessedWord(secretWord, lettersGuessed))
        elif guess in oldGuessList:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        else:
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            i -= 1
        # update the guessList, in case the user type the same letter
        oldGuessList.append(guess)
        if isWordGuessed(secretWord, lettersGuessed):
            print('-------------')
            print('Congratulations, you won!')
            break
        else:
            if i == 0:
                print('-------------')
                print('Sorry, you ran out of guesses. The word was else.')
                break



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
