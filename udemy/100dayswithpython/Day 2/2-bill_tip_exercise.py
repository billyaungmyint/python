print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10,12 or 15? ")) / 100
num_of_people = int(input("How many people to split the bill? "))

final_bill = (total_bill +  (total_bill * tip_percent)) / num_of_people

print(f"Each person should pay: ${round(final_bill , 2)}")