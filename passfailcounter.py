students=[]
roll_no=[]
marks=[]
passcount=0
failcount=0
while True:
    student=input("Enter The Student Name(q to quit): ")
    if student.lower()=="q":
        break
    else:
        rollno=int(input("Enter The Roll No: "))
        mark=int(input("Enter The Mark: "))
        students.append(student)
        roll_no.append(rollno)
        marks.append(mark)
print("-----MARK LIST-----")
print(f"{'NAMES':<15}{'ROLL_N0':<10}{'MARKS':<6}")
for student,rollno,mark in zip(students,roll_no,marks):
    print(f"{student:<15}{rollno:<10}{mark:<6}")
for mark in marks:
    if mark>=35:
        passcount+=1
    else:
        failcount+=1
        
print(f"Number Of Students Paased is {passcount}.")
print(f"Number Of Students Failed s {failcount}.")
    
