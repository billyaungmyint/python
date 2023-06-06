import re

x = 'From: billy@billyaungmyint.com Sat 09:50'
# \S+ 1 or more non-space characters
# @ @ sign
# \S+ 1 or more non-space characters
y = re.findall('\S+@\S+' , x)
print(y)
# the line must starts with From
y = re.findall('^From: (\S+@\S+)' , x)
print(y)