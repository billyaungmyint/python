from beatles_imagine import imagine

imagine = imagine.lower().split(' ')


# 1 - create a frequency mapping dict:int

def lyrics_to_frequencies(lyrics):
    mydict = {}
    for word in lyrics:
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1

    return mydict


beatles = lyrics_to_frequencies(imagine)


# 2 - find words the occurs the most and how many times
def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)

    return words, best


(w, b) = most_common_words(beatles)


# 3 - find the words that occur at least x times
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del (freqs[w])
        else:
            done = True
    return result


print(words_often(beatles, 2))
