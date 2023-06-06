# number1 = int(input("What is the first number? : "))
# number2 = int(input("What is the second number? : "))
# operation = input("What is the operation? : ")

# def my_func(number1,number2,operation):
#     if operation == "+":
#         return number1 + number2
#     elif operation == "-":
#         return number1 - number2
#     elif operation == "*":
#         return number1 * number2
#     elif operation == "/":
#         return number1 / number2
#     else:
#         print("Pls enter only + - * or /")

# output = my_func(number1,number2,operation)
# print(output)

def format_name(f_name ,l_name):
    return str(f_name).title() + " " + str(l_name).title()

print(format_name("BILLY","aung"))