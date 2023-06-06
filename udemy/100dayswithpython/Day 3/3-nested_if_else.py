print("Welcome to the rollercoaster!!")
height = int(input("What is your height in cm? "))

# if height > 120:
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("WHat is your age? "))
    if age < 12:
        print("Pls pay $5")
    elif age <= 18:
        print("Pls pay $7")
    else:
        print("pls pay $12")
else:
    print("Sorry , you get to be taller before you can ride.")