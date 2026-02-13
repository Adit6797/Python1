students = []
for i in range(1, int(input("Enter the number of student="))+1):
        name = input(f"Enter name of student{i}=")
        score = float(input(f"enter score of student{i}="))
        student=[name,score]
        students.append(student)
print(students)