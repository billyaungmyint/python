import pandas as pd
import random


# get the past winning numbers from the web
url = 'https://en.lottolyzer.com/history-export-csv/singapore/toto/ToTo.csv'
# read the url
data = pd.read_csv(url)
# make a lit of 1 - 49 numbers - the numbers that are in the TOTO
all_numbers = list(range(1, 50))
unlucky_numbers = [8,10,11,25,37,38,44] # manual entry ,  otherwise blank

def removeNumbersFromList(l1, l2):
    return [x for x in l1 if x not in l2]

def flatten(l):
    return [item for sublist in l for item in sublist]


def list2size(lst, sizes):
    random.shuffle(lst)
    ret = []
    pointer = 0
    for s in sizes:
        ret.append(lst[pointer:pointer + s])
        pointer += s
    return ret


# from the data , choose the specific columns from there , winning numbers + additional number
winning_number = data[['Winning Number 1', '2', '3', '4', '5', '6', 'Additional Number ']]
# rename the winning number and additional number columns to 1 and 7 respectively
winning_number = winning_number.rename({'Winning Number 1': '1', 'Additional Number ': '7'}, axis=1)

# winning_number5 = winning_number.iloc[0:5]
# winning_number10 = winning_number.iloc[0:10]
# transposed_winning_number5 = winning_number5.transpose()
# transposed_winning_number10 = winning_number10.transpose()

# make a new list of winning numbers of the most recent 10 winning numbers 
winning_list = winning_number.iloc[0:3].values.tolist()
winning_list2 = flatten(winning_list)
# remove the past winning numbers from the 1-50 list - since past winnings are usually not repeated
final_list1 = removeNumbersFromList(all_numbers, winning_list2)
# remove the unlucky numbers - manual entry. otherwise , blank 
final_list = removeNumbersFromList(final_list1 , unlucky_numbers)

# final list
test = []
# print a list of 5 lists of 6 numbers each
for i in range(3): # 5 is how many list of numbers 
    test.append(list2size(final_list,sizes = [7])) # 6 is the number of items within each sublist - if system 7 , then put 7.
#print(winning_number10)
#print('After transposed')
# print(transposed_winning_number10)
print(flatten(test))
