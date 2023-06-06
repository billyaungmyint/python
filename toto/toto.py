import numpy as np
import pandas as pd
import random

url = 'https://en.lottolyzer.com/history-export-csv/singapore/toto/ToTo.csv'
data = pd.read_csv(url)
all_numbers = list(range(1, 50))


def removelast5(l1, l2):
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


winning_number = data[['Winning Number 1', '2', '3', '4', '5', '6', 'Additional Number ']]
winning_number = winning_number.rename({'Winning Number 1': '1', 'Additional Number ': '7'}, axis=1)

winning_number5 = winning_number.iloc[0:5]
winning_number10 = winning_number.iloc[0:10]
transposed_winning_number5 = winning_number5.transpose()
transposed_winning_number10 = winning_number10.transpose()

winning_list = winning_number.iloc[0:10].values.tolist()
winning_list2 = flatten(winning_list)
final_list = removelast5(all_numbers, winning_list2)

test = []
for i in range(4):
    test.append(list2size(final_list,sizes = [6]))
print(test)
# print(winning_number10)
# print('After transposed')
# print(transposed_winning_number10)444444444444444444444444444