animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(f"Original animals : {animals}")


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    total = 0
    for value in aDict:
        if len(aDict[value]) == 1:
            total += 1
        else :
            total += len(aDict[value])

    return total

print(how_many(animals))
