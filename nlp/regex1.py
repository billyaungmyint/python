import re

# print(re.search("Sheep", "One sheep"))
# print(re.search("sheep", "One sheep , two sheep"))
#
# match = re.search('sheep', 'one sheep , two sheep')
# print(match.group())


def find_pattern(text, pattern):
    return re.search(pattern, text)

print(find_pattern('one sheep , two sheep' , 'sheep'))
print(find_pattern('one sheep , two sheep' , 'she*'))
print(find_pattern('one sheep , two sheep' , 'sh*'))
print(find_pattern('one sheep , two sheep' , 's'))
print(find_pattern('ac' , 'ab*'))
print(find_pattern('abc' , 'ab*'))
print(find_pattern('abbc' , 'ab*'))
