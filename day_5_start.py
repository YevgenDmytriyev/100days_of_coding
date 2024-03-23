# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#156 178 165 171 187

#Write your code below this row 👇
total_of_students = 0
for i in student_heights:
    total_of_students += 1

total_height = 0
for i in student_heights:
    total_height += i 
print(total_of_students)
avarage_height = round(total_height / total_of_students)

#total_height = sum(student_heights)
#number_of_students = len(student_heights)
#avarage_height = round(total_height / number_of_students)
#print(avarage_height)
print(avarage_height)




