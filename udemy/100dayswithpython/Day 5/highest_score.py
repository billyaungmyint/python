#student_scores = [78 , 65 , 89 , 86 , 55 , 91 , 64 , 89]
student_scores = input("Pls enter the scores : ").split()
highest = 0

# for score in student_scores:
#     if int(score) > int(highest) :
#         highest = score

#or use max
highest = max(student_scores)
print(f"Highest score is : {highest}")