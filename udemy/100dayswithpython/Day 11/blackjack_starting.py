from art import logo
import random

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_another_game = True
while play_another_game == True:
    def deal_card():
        random_index = random.randint(0,len(cards) -1 )
        return cards[random_index]



    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    #user_cards = []
    computer_cards = []
    user_cards = []

    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
    user_cards.append(deal_card())

    # print(computer_cards)
    # print(user_cards)

    #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
    #and returns the score. 
    #Look up the sum() function to help you do this.

    cards_dealt = []


    def calculate_score(cards_dealt):
        for x in cards_dealt:
            if x == 11:
                cards_dealt.remove(x)
                cards_dealt.append(1)
                
        if sum(cards_dealt) != 21:
            return sum(cards_dealt)
        else :
            return 0
        
    user_score = calculate_score(user_cards)
    com_score = calculate_score(computer_cards)
    user_continue = True

    while user_continue == True : 
        if user_score == 0 or com_score == 0:
            print(f"User's score is : {user_score}")
            print(f"Computer's score is : {com_score}")
            print("Blackjack!")
            user_continue = False
        else:
            print(f"Your score now is : {user_score}")
            if user_score <= 21:
                draw_next = input("Draw another card? y or n : ")
                if  draw_next == 'n':
                    #print("The game has ended")
                    user_continue = False
                else :
                    user_cards.append(deal_card())
                    user_score = calculate_score(user_cards)
                    user_continue = True
            else:
                print("Sorry. You lose!")
                user_continue = False

    while com_score < 17:
        computer_cards.append(deal_card())
        com_score = calculate_score(computer_cards)
        
    def print_scores():
        print(f"User's score is {user_score}")
        print(f"Computer's score is {com_score}")
        
    def compare(user_score , com_score):
        if user_score == com_score:
            print_scores()
            print("Its a draw!!!")
        elif user_score == 0:
            print("Blackjack! User wins!")
        elif com_score ==0:
            print("Backjack! Computer wins!")
        elif user_score > 21:
            print_scores()
            print("User's score is more than 21. Computer wins!")
        elif com_score > 21:
            print_scores()
            print("Computer's score is more than 21. User wins!")
        elif user_score > com_score:
            print_scores()
            print("User has higher score! User wins!")
        elif com_score > user_score:
            print_scores()
            print("Computer has higher score! Computer wins!")

    compare(user_score , com_score)
    
    play_next = input("Do you want to play another game? y or n : ")
    if play_next == 'y':
        play_another_game = True
    elif play_next == 'n' :
        print("Thank you for playing. Goodbye!")
        play_another_game = False


    # print(calculate_score(user_cards))

    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

    #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

    #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
