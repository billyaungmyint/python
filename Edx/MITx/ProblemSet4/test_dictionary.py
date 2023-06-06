from ps4a import *

# sum = 0
# word = "fork" # 94
# n = 4

#
# for i in word:
#     sum += SCRABBLE_LETTER_VALUES[i]
#
# print(sum)
# sum = sum * len(word)
#
# if len(word) == 7:
#     sum += 50
#
# if len(word) == n:
#     sum += 50
#
# print(sum)
hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
# print(hand.get('g' , 0))

# hand = dealHand(7)
# displayHand(hand)
# print(hand['l'])
#
# def updateHand(hand, word):
#     new_hand = hand.copy()  # or hand[:]
#     for i in word:
#         new_hand[i] -= 1
#     return new_hand


#print(updateHand(hand, 'quail'))  # You implement this function!
#print(wordlist)


# def isvalidword(word , hand, wordlist):
#     xCopy = hand.copy()
#     if word in wordlist:
#         for letter in word:
#             if letter in xCopy:
#                 if xCopy[letter] == 0:
#                     return False
#                 else:
#                     xCopy[letter] -= 1
#             else:
#                 return False
#     else:
#         return False
#
#     # Return True if all of the above works out.
#     return True
#
# print(isvalidword(word , hand, wordlist))


#
# def calculateHandlen(hand):
#     """
#     Returns the length (number of letters) in the current hand.
#
#     hand: dictionary (string-> int)
#     returns: integer
#     """
#     no_of_letters = 0
#
#     for i in hand:
#         no_of_letters += hand[i]
#
#     return no_of_letters
#
# print(calculateHandlen(hand))

word = 'hello'
hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
wordlist = loadWords()


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while True:
    # Display the hand

    # Ask user for input

    # If the input is a single period:

    # End the game (break out of the loop)

    # Otherwise (the input is not a single period):

    # If the word is not valid:

    # Reject invalid word (print a message followed by a blank line)

    # Otherwise (the word is valid):

    # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line

    # Update the hand

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score