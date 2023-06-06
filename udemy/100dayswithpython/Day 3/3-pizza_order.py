print("Welcome to the Pizza Ordering System.")
pizza_size = input("What size of pizza you would like? S ,  M , or L : ")
add_pepperoni = input("Would you like to add pepperoni? Y or N : ")
extra_cheese = input("Would you like to add extra cheese? Y or N : ")
bill = 0

if pizza_size == 'S' :
    bill += 15
    if add_pepperoni =='Y' :
        bill += 2
    if extra_cheese == 'Y' :
        bill += 1
if pizza_size == 'M' :
    bill += 20
    if add_pepperoni == "Y" : 
        bill += 3
    if extra_cheese == 'Y' :
        bill += 1
if pizza_size == 'L' :
    bill += 25
    if add_pepperoni == "Y" : 
        bill += 3
    if extra_cheese == 'Y' :
        bill += 1

print(f"The final bill for a {pizza_size} is ${bill}")
    