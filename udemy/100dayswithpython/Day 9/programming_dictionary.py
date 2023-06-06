programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}

test_dict = {
    1: "Test One",
    "Hello": "Hello Billt"
}

test_dict["Hello"] = "Replaced Hello"
test_dict["Goodbye"] = "New Goodbye"
for key in test_dict:
    print(key)
    print(test_dict[key])
    