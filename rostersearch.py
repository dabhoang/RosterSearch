import sys
import csv

def search_name(pattern): #searches for pattern in all students' first names and last names
    print("Searching for all students with \"" + sys.argv[2] + "\" in their first name or last name:")
    for student in students[1:]:
        student_firstname = student[0].lower() #gets the student's first name from csv file and ensures case insensitivity
        student_lastname = student[1].lower() #gets the student's last name from csv file and ensures case insensitivity
        if(student_firstname.find(pattern) != -1): #determines if the pattern exists in the first name and prints the student if so
            print(student)
        if(student_lastname.find(pattern) != -1): #determines if the pattern exists in the last name and prints the student if so
            print(student)

def search_email(pattern): #searches for pattern in all students' emails without "@ucdavis.edu" suffix
    print("Searching for all students with \"" + sys.argv[2] + "\" in their email without the \"@ucdavis.edu\" suffix:")
    for student in students[1:]:
        emailbase = student[2].replace("@ucdavis.edu","").lower() #gets rid of "@ucdavis.edu" suffix and ensures case insensitivity
        if(emailbase.find(search_pattern) != -1): #determines if the pattern exists in the email base and prints the student if so
            print(student)

def search_gpa(gpa): #searches for students with certain gpa's or gpa's in the specified range based on suffix
    if gpa[-1] == '+': #suffix is a '+', print all students with gpa's >= the entered gpa
        gpa = gpa.replace("+","") #gets rid of suffix
        check_gpa_is_float(gpa)
        print("Searching roster for students with a gpa of " + gpa + " and above:")
        for student in students[1:]:
            if student[3] >= gpa: #print all students with gpa's greater then or equal to the entered gpa
                print(student)

    elif gpa[-1] == '-': #suffix is a '-', print all students with gpa's <= the entered gpa
        gpa = gpa.replace("-","") #gets rid of suffix
        check_gpa_is_float(gpa)
        print("Searching roster for students with a gpa of " + gpa + " and below:")
        for student in students[1:]: 
            if student[3] <= gpa: #print all students with gpa's less than or equal to the entered gpa
                print(student)

    else: #no suffix
        check_gpa_is_float(gpa)
        print("Searching roster for students with a gpa of " + gpa + ":")
        for student in students[1:]: 
            if student[3] == gpa: #print all students with gpa's equal to the entered gpa
                print(student) 

def check_gpa_is_float(gpa): #make sure that the gpa entered by the user without the suffix is indeed a float followed by an optional suffix
    try: 
        float(gpa)
    except:
        print("Please enter gpa in the form of a float followed by an optional suffix of \'+\' or \'-\'")
        roster.close() #close the csv file
        exit()

#main program execution begins

if(len(sys.argv) != 4): #makes sure that the number of arguments are correct
    print('''Please make sure that there are three command line arguments following rostersearch.py.

    The first one should be one of:
    -name
    -email
    -gpa
    
    The second one should be one of:
    a pattern to search for if the previous command line argument was -name or -email
    a float followed by an option suffix of '+' or '-' if the previous command line argument 
    
    And finally the last one should be the name of the csv file containing the roster for which the search is to be performed on.''')
    exit()
    
if(sys.argv[3].endswith(".csv") is False): #last command line argument should be the name of the roster file
    print("The last command line argument must be a csv file containing the roster with a suffix of \".csv\"")
    exit()

roster = open(sys.argv[3], 'r', encoding = 'utf-8') #open the csv file
students = list(csv.reader(roster)) #students is a list of all students
search_pattern = sys.argv[2].lower() #ensures that our searches are case insensitive

#determines the function for appropriate column(s) to search based on command
if sys.argv[1] == "-name": #command is “-name <pattern>”
    search_name(search_pattern)
elif sys.argv[1] == "-email": #command is “-email <pattern>”
    search_email(search_pattern)
elif sys.argv[1] == "-gpa": #command is “-gpa <gpa>[+-]”
    search_gpa(search_pattern)

else: print("Please enter -name -email or -gpa as the first command line argument after rostersearch.py") #first command line argument after rostersearch.py should be -name, -email, or -gpa

roster.close() #close the csv file