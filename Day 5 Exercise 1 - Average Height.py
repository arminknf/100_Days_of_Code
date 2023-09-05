# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#print(student_heights)
#print(n)
number_student = 0

for student in student_heights:
  number_student += 1
#print(number_student)

height_sum = 0 
for height_item in student_heights:
  height_sum = height_sum + height_item
print(height_sum)

average_height = (height_sum/number_student)
average_height_rounded = round(average_height)
print(average_height_rounded)
#print(f"Average heights rounded to the nearest whole number = {average_height_rounded}")



