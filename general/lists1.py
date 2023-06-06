robots = {}
newline = []

file = open('cards.txt', 'r')
i = 0

for line in file.read().splitlines():
   newline[i] = line.split(', ')
   robots[name] = [battery,intelligence,image]
   print(line)
   print(newline[i])


file.close()