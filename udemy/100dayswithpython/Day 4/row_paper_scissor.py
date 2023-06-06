import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#computer choose 0,1,2 corresponding to rock , paper or scissor
com_choose = random.randint(0,2)
user_choose = int(input("Type 0 for Rock , 1 for Paper and 2 for Scissor :  "))
rps = ["Rock" , "Paper" , "Scissors"]
rps_image = [rock , paper, scissors]
#print(f"com choose {rps[com_choose]} and user choose {rps[user_choose]}\n")
print(f"\nComputer chose {rps[com_choose]}\n")
print(rps_image[com_choose])
print(f"You chose {rps[user_choose]}\n")
print(rps_image[user_choose])

if com_choose == 0 and user_choose == 0:
    print("DRAW!!!")
elif com_choose == 0 and user_choose == 1:
    print("You Win!!!")
elif com_choose == 0 and user_choose == 2:
    print("You Lose!!!")
elif com_choose == 1 and user_choose == 0:
    print("You Lose")
elif com_choose == 1 and user_choose == 1:
    print("Draw")
elif com_choose == 1 and user_choose == 2:
    print("You Win!!!")
elif com_choose == 2 and user_choose == 0:
    print("You Win!!")
elif com_choose == 2 and user_choose == 1:
    print("You Lose!!!")
elif com_choose == 2 and user_choose == 2:
    print("Draw!!!")
else :
    print("Pls enter number between 0 and 2!!")
 
