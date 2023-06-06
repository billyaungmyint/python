vowel = 'aeiou'
total_vowels = 0
s = 'xkjqbeinlkhqpmvdx'

for x in range(len(s)) :
    if s[x] in vowel :
        total_vowels += 1


print('Number of vowels: ' + str(total_vowels))