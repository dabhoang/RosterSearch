import sys
import csv

if(len(sys.argv) != 4):
    print("Please enter arguments of the format...")
    exit()

roster = open(sys.argv[3], 'r', encoding = 'utf-8')
students = list(csv.reader(roster))

if sys.argv[1] == "-name":
    print("name")
    search_pattern = sys.argv[2].lower()
    for student in students[1:]:
        
        student_firstname = student[0].lower()
        student_lastname = student[1].lower()
        print(search_pattern)
        if(student_firstname.find(search_pattern) != -1):
            print(student)
        if(student_lastname.find(search_pattern) != -1):
            print(student)

elif sys.argv[1] == "-email":
    print("email")
    search_pattern = sys.argv[2].lower()
    for student in students[1:]:
        emailbase = student[2].replace("@ucdavis.edu","").lower()
        if(emailbase.find(search_pattern) != -1):
            print(student)
elif sys.argv[1] == "-gpa":
    print("gpa")
    
    if sys.argv[2][-1] == '+':
        gpa = sys.argv[2].replace("+","")
        print(gpa)
        for student in students[1:]:
            if student[3] >= gpa:
                print(student)

    elif sys.argv[2][-1] == '-':
        gpa = sys.argv[2].replace("-","")
        print(gpa)
        for student in students[1:]:
            if student[3] <= gpa:
                print(student)
    else:
        for student in students[1:]:
            if student[3] == gpa:
                print(student)

else: print("Please enter -name -email or -gpa")

roster.close()