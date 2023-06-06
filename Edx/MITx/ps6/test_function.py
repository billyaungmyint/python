import string

message_text = "Hello"

def build_shift_dict(shift):
    # create a new dict
    aDict = {}

    # loop through the string
    for letter_index in range(len(string.ascii_lowercase)):
        if letter_index <= 25 - shift:
            aDict[string.ascii_lowercase[letter_index]] = string.ascii_lowercase[letter_index + shift]
            aDict[string.ascii_uppercase[letter_index]] = string.ascii_uppercase[letter_index + shift]
        else:
            aDict[string.ascii_lowercase[letter_index]] = string.ascii_lowercase[letter_index - 26 + shift]
            aDict[string.ascii_uppercase[letter_index]] = string.ascii_uppercase[letter_index - 26 + shift]

    return aDict

def apply_shift(shift):

    # create a new list
    aList = []
    # go through each char in the message text to encrypt
    for char in "Hello":
        #print(char)
        try:
            aList.append(build_shift_dict(shift)[char])
        except:
            aList.append(char)

    return ''.join(aList)

print(apply_shift(2))
print(build_shift_dict(2)['a'])