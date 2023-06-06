from art import logo
import os

print(logo)


other_bidders = "no"
bid_log = []
highest_bidder = ""
highest_bid_price = 0

def add_bid(name,bid):
    bid_log.append({name,bid})

# bid_log = [
# {
#     "Name": "Billy" , 
#     "Bid_price" : 32
# },
# {
#     "Name" : "James",
#     "Bid_price" : 19
# }
# ]

def check_highest_bid(bid_log):
    for x in range(0,len(bid_log)):
        #print(bid_log[x]["Bid_price"])
        #highest_bid_price = bid_log[x]["Bid_price"]
        if bid_log[x]["Bid_price"] > highest_bid_price:
            highest_bidder = "Billy"
            highest_bid_price = bid_log[x]["Bid_price"]
    clear_screen()
    print(f"The highest bid of {highest_bid_price} was submitted by {highest_bidder}")
         
def bidding_process():
    other_bidders = "no"
    if other_bidders == "no":
        check_highest_bid(bid_log)
    elif other_bidders == "yes":
        bidder_name = input("What is your name? : ")
        bid_price = int(input("What is your bid? : "))
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no' : " )
        add_bid(bidder_name,bid_price)





#clear screen
def clear_screen():
    clear = lambda: os.system('cls')
    clear()
#################### her code ################

from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()