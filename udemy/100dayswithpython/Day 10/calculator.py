# calculator

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

answer = 0
to_continue = True
num1 = int(input("Pls enter the first number : "))
for x in operations:
    print(x)

while to_continue == True:
    operational_symbol = input("Pick an operation. : ")
    num2 = int(input("Pls enter the next number : "))
    calculation_function = operations[operational_symbol]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operational_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type'n' to exit : ") == "y":
        num1 = answer
    else: 
        to_continue = False
        print("Goodbye!")


