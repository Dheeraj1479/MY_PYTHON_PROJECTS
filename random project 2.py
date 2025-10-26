e1 = int(input("Enter marks: "))
e2 = int(input("Enter marks: "))
e3 = int(input("Enter marks: "))
total_marks = e1 + e2 + e3

essay_late = int(input("Enter number of essays handed in late: "))

if essay_late == 1:
    total_marks -= 10
elif essay_late > 1:
    total_marks /= 2

if total_marks < 0:
    total_marks = 0 

print(int(total_marks))