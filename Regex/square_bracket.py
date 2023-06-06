import re

x = 'My 2 fav numbers are 18 and 42'
# 1 or more digit
# y = re.findall('[0-9]+' , x)
# y = re.search('[0-9]' ,x)
y = re.findall('[0-9]' , x)
print(y)
y = re.findall('[AEIOU]+' , x)
print(y)
print(len(y))
