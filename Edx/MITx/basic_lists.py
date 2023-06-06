list1 = [55,87,665,11,30]
list2 = [1,2,"Three" , 4]
total = 0

for i in list1 :
    total += i
print(f"List1 total is : {total}")

print('')

for x in range(len(list2)) :
    print(f"List 2 contains : {list2[x]}")

L = [1,2,3]
L.append(5)
print(f"L is now : {L}")
L.extend([2,3])
print(f"L is now : {L}")

del(L[1])
print(f"After del() L is now : {L}")
L.pop()
print(f"After pop() L is now : {L}")
L.remove(2)
print(f"After remove(2) L is now : {L}")
print('')

s = 'I <3 CS'
print(f"Original s : {s}")
list(s)
print(f"After list(s) s is now : {s}")
s.split('<')
print(f"After split() s is now : {s}")
print('')

L = ['a','b','c']
print(f"Original L : {L}")
''.join(L)
print(f"After join L is now : {L}")
'_'.join(L)
print(f"After join L is now : {L}")
print('')

L = [2,5,3]
print(f"Original L : {L}")
sorted(L)
print(f"After sorted L is now : {L}")
L.sort()
print(f"After sort L is now : {L}")
L.reverse()
print(f"After reverse L is now : {L}")
L.insert(0, 100)
print(f"After insert L is now : {L}")
L.count(2)
print(f"After count L is now : {L}")