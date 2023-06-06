print("Welcome to the love calculator")
name1 = input("What is your name? : ")
name1_lower = name1.lower()


name2 = input("What is your name? : ")
name2_lower = name2.lower()

combined_name = name1_lower + name2_lower
combine_score = 0

#print(f"combined name is {combined_name}")
#how many charactes in the name belongs to TRUE LOVE

score_t = combined_name.count("t")
score_r = combined_name.count("r")
score_u = combined_name.count("u")
score_e = combined_name.count("e")
score_l = combined_name.count("l")
score_o = combined_name.count("o")
score_v = combined_name.count("v")

true_score = score_t + score_r + score_u + score_e
love_score = score_l + score_o + score_v + score_e

total_score = str(true_score) + str(love_score)

print(f"The letter T occured {score_t} times")
print(f"The letter R occured {score_r} times")
print(f"The letter U occured {score_u} times")
print(f"The letter E occured {score_e} times")
print(f"The letter L occured {score_l} times")
print(f"The letter O occured {score_o} times")
print(f"The letter V occured {score_v} times")
print(f"The letter E occured {score_e} times")

print(f"Your final love score is {total_score}")
