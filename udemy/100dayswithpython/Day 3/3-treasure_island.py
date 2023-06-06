print("Welcome to the treasure Island.\n")
print("Your mission is to find the treasure.\n")
left_right = input("Pls choose whether to go to left or right : ")
if left_right.lower() == "left" :
    swim_wait = input("Swim or Wait? : ")
    if swim_wait.lower() == "wait" :
        rbg = input("Which door? Red , Blue or Yellow ? : ")
        if rbg.lower() == "yellow" :
            print("You have found the treasure!!")
        else:
            print("Game Over. Worong door!!")
    else:
        print("Game Over. You have been eaten by a shark!!")
else:
    print("Game Over. You feell in to a hole!!!")
