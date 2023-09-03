# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#print(student_heights)
#print(n)

sum_score = 0
for score in student_heights:
    sum_score = score + sum_score
#print (sum_score)#int
#print (n)#int

#average_score = (sum_score / (n+1))
number_of_students =  0
for student in student_heights:
    number_of_students += 1

average_score = (sum_score / number_of_students)

avg_score_rnd = round(average_score)
print(avg_score_rnd)



