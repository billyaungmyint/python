import art
from game_data import data
import random

celebrity = {}
celebrity_name = ""
celebrity_follower_count = 12
celebrity_country = ""
celebrity_description = ""


right_or_wrong = True

#print(f"The celebrity 1 - {celebrity1_name} is a {celebrity1_description} from {celebrity1_country}")
#print(f"The celebrity 2 - {celebrity2_name} is a {celebrity2_description} from {celebrity2_country}")



def generate_random_celebrity():
    random_index = random.randint(0,49)
    celebrity_name = data[random_index]["name"]
    celebrity_follower_count = data[random_index]["follower_count"]
    celebrity_description = data[random_index]["description"]
    celebrity_country = data[random_index]["country"]
    celebrity = {
        "name" :celebrity_name , 
        "follower_count" : celebrity_follower_count , 
        "description" : celebrity_description , 
        "country" : celebrity_country
    }
    return celebrity

c1 = {}
c2 = {}
c3 = {}

def celebrity_with_more_followers(c1 , c2):
    c1_followers = c1["follower_count"]
    c2_followers = c2["follower_count"]
    if c1_followers > c2_followers:
        return c1
    elif c2_followers > c1_followers:
        return c2


# print(f"c1 - {c1['name']} has {c1['follower_count']} followers.")
# print(f"c2 - {c2['name']} has {c2['follower_count']} followers.")
# print(f"c3 - {c3['name']} has {c3['follower_count']} followers.")


def play_game (c1 , c2 , c3):
    global right_or_wrong1
    print(art.logo)
    print(f"{c1['name']}")
    print(art.vs)
    print(f"{c2['name']}\n")
    user_choice = int(input(f"Who has more instagram followers ? 1 or 2 : "))
    if user_choice == 1 :
        if c3 == c1 :
            right_or_wrong = True
            print("You are right!\n")
        elif c3 == c2:
            right_or_wrong = False
            print("You are wrong!\n")
    elif user_choice == 2:
        if c3 == c1:
            right_or_wrong = False
            print("You are wrong!\n")
        elif c3 == c2:
            right_or_wrong = True
            print("You are right!\n") 
            
while right_or_wrong == True :
    c1 = generate_random_celebrity()
    c2 = generate_random_celebrity()
    c3 = celebrity_with_more_followers(c1,c2)
    play_game(c1 , c2 , c3)