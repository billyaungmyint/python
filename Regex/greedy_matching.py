import re

x = 'From: Using the : character'
# ^F Starts with capital F
# .+ 1 or more of characters
# : last character in a match
y = re.findall('^F.+:' , x)
print(y)