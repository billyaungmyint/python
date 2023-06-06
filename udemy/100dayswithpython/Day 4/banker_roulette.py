import random

# only split when you are using input from console.
# if use the list hardcoded , no need to split
#bankers_input = input("Pls enter the names : ")
#bankers_names = bankers_input.split(", ")

bankers_names = ["Billy" , "James", "Angela" , "Tom" , "Ford"]
print(bankers_names)
no_of_bankers = len(bankers_names)
#print(no_of_bankers)
# or use random.choice() 
pay_the_bill = bankers_names[random.randint(0,no_of_bankers-1)]
print(f"{pay_the_bill} is paying the bill!")