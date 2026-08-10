students=[]
roll_nos=[]
marks=[]
grades=[]

while True:
    student=input("Enter The Name(q to quit): ")
    if student=="q":
        break
    else:
        roll_no=int(input("Enter The Roll number: "))
        mark=int(input("Enter The Marks: "))
        students.append(student)
        roll_nos.append(roll_no)
        marks.append(mark)
for mark in marks:
    if mark>=90:
        grade='A'
    elif mark>=75:
        grade='B'
    elif mark>=50:
        grade='c'
    else:
        grade='F'
    grades.append(grade)
print(f"{'NAMES':<15}{'ROLL_NO':<10}{'MARKS':<6}{'GRADES':<10}")
for student,roll_no,mark,grade in zip(students,roll_nos,marks,grades):
    print(f"{student:<15}{roll_no:<10}{mark:<6}{grade:<10}")
topper_name=""
topper_roll=0
topper_mark=-1
for student,roll_no,mark in zip(students,roll_nos,marks):
    if mark>topper_mark:
        topper_name=student
        topper_roll=roll_no
        topper_mark=mark
print(f"TOPPER:{topper_name},ROLL NO:{topper_roll},Marks:{topper_mark}")
    

    
