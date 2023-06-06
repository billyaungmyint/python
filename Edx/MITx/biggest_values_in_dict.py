animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
aDict = {'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]}
aDict2 = {'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': [18]}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    values = aDict.values()
    value_size = []
    largest = 0
    largest_key = ''
    for i in values :
        value_size.append(len(i))

    largest = max(value_size)

    for key, value in aDict.items():
        if len(value) == largest :
            largest_key = key

    return largest_key


print(biggest(aDict2))
