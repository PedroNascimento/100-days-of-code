# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# The algorithm below calculates the sum of the students' heights
total_height = 0
for height in student_heights:
    total_height += height

# The algorithm below adds up the number of students who entered their heights.
number_of_students = 0
for student in student_heights:
    number_of_students += 1

media_height = total_height / number_of_students
print(round(media_height))
