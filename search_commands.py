def search_name(pattern, students): #searches for pattern in all students' first names and last names
    print("Searching for all students with \"" + pattern + "\" in their first name or last name:")
    pattern = pattern.lower() #ensures that our searches are case insensitive
    for student in students[1:]:
        student_firstname = student[0].lower() #gets the student's first name from csv file and ensures case insensitivity
        student_lastname = student[1].lower() #gets the student's last name from csv file and ensures case insensitivity
        if(student_firstname.find(pattern) != -1): #determines if the pattern exists in the first name and prints the student if so
            print(student)#"Name: " + student[0] + " " + student[1] + ", Email: " + student[2] + ", GPA: " + student[3])
        elif(student_lastname.find(pattern) != -1): #determines if the pattern exists in the last name and prints the student if so
            print(student)

def search_email(pattern, students): #searches for pattern in all students' emails without "@ucdavis.edu" suffix
    print("Searching for all students with \"" + pattern + "\" in their email without the \"@ucdavis.edu\" suffix:")
    pattern = pattern.lower() #ensures that our searches are case insensitive
    for student in students[1:]:
        emailbase = student[2].replace("@ucdavis.edu","").lower() #gets rid of "@ucdavis.edu" suffix and ensures case insensitivity
        if(emailbase.find(search_pattern) != -1): #determines if the pattern exists in the email base and prints the student if so
            print(student)

def search_gpa(gpa, students): #searches for students with certain gpa's or gpa's in the specified range based on suffix
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