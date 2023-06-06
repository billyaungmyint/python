import random

row1 = ["O","O","O"]
row2 = ["O","O","O"]
row3 = ["O","O","O"]
map = [row1 , row2 , row3]
print(f"before changing\n\n{row1}\n{row2}\n{row3}\n\n")

#user entered 23
#row 2 column 3 changed to X

#user_entered = int(input("Pls enter 2 digits : "))
# user_entered = int(str(random.randint(1,3)) + str(random.randint(1,3)))
# row_to_change = int(user_entered / 10)
# column_to_change = int(user_entered % 10)
user_entered = str(random.randint(1,3)) + str(random.randint(1,3))
row_to_change = int(user_entered[0])
column_to_change = int(user_entered[1])

print(f"row to change is {row_to_change} and column to change is {column_to_change}\n\n") 

row_to_change = row_to_change - 1
column_to_change = column_to_change - 1 
map[row_to_change][column_to_change] = "X"

# if row_to_change == 0:
#     if column_to_change ==0 :
#         row1 = ["X" , "O" , "O"]
#     if column_to_change == 1:
#         row1 = ["O" , "X" , "O"]
#     if column_to_change == 2:
#         row1 = ["O" , "O" , "X"]
# if row_to_change == 1:
#     if column_to_change ==0 :
#         row2 = ["X" , "O" , "O"]
#     if column_to_change == 1:
#         row2 = ["O" , "X" , "O"]
#     if column_to_change == 2:
#         row2 = ["O" , "O" , "X"]
# if row_to_change == 2:
#     if column_to_change ==0 :
#         row3 = ["X" , "O" , "O"]
#     if column_to_change == 1:
#         row3 = ["O" , "X" , "O"]
#     if column_to_change == 2:
#         row3 = ["O" , "O" , "X"]
        
print(f"After changing\n\n{row1}\n{row2}\n{row3}\n\n")