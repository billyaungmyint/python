print([ i for i in range(15) if i%2 ==0])
print([ i**2 for i in range(15) if i%2 ==0])

print([i for i in range(15)])
print()

# not include then "hi"
print([i if i%2 ==0 else "hi" for i in range(15)])
print()

namesDict = {"Nora": 56, "Lulu": 15, "Gino": 31}
print([value for value in namesDict.values() if value % 2 != 0])
print()

grades = {"Nora": 90, "Lulu": 15, "Gino": 60}
print({key: value*2 for (key, value) in grades.items()})