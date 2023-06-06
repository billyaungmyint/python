listA = [1,2,3,4,5]
listB = listA
listB.append(6)

print(f"listA is : {listA}")
print(f"listB is : {listB}")
print(f"listA == listB : {listA == listB}")
print(f"list A is listB : {listA is listB}")
print()

listC = listA[:]
print(f"listC is : {listC}")
print("pop listA")
listA.pop()

print(f"listA after pop() is : {listA}")
print(f"listB after pop() is : {listB}")
print(f"listC after pop() is : {listC}")
print("now listA and listB changed but not listC because C is a copy/clone of A and not pointing to the same address as A.")
print()

print(f"After pop , listA == listB : {listA == listB}")
print(f"After pop , list A is listB : {listA is listB}")
print(f"After pop , list C == listA : {listC == listA}")
print(f"After pop , list C is listA : {listC is listA}")