students_height= [180 ,124 , 165,173 , 189,169,146]

summ = 0
avg = 0
total = 0

# for height in students_height:
#     sum += height
#     total += 1

#or use sum and len 
summ = sum(students_height)
total = len(students_height)
avg = round(summ / total)
print(f"The average height of {total} students is {avg}")