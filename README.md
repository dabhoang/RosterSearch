To execute this python script, clone the RosterSearch repository from dabhoang's github. Move the csv file containing the roster for which the search is to be performed into the RosterSearch directory.

When entering student information into your csv file, please do not include any students in the first line. The script is designed to begin searching the second line so that the first line can list the column titles/headers. And please ensure that the first column is for first names, the second column is for last names, the third column is for emails, and the fourth column is for gpa's. An example roster is provided in the repository.

Run the cd command on the terminal into the RosterSearch directory and then run the following command with replacements for arg1, arg2, and arg3 once inside RosterSearch:

py rostersearch.py arg1 arg2 arg3 

arg1, arg2, and arg3 are replaced with the following:

arg1 is one of: -name -email or -gpa 
Use -name to search for all students with a certain pattern in their first or last names in the roster, case insensitive
Use -email to search for a pattern in all students with a certain pattern in their email without @ucdavis.edu in the roster, case insensitive
Use -gpa to search for all students with a certain gpa. A gpa floor or ceiling can also be applied. 

arg2 will depend on arg1. 

If arg1 was -name or -email then arg2 should be the pattern to search for in each name or email. 
For example, if I wanted to search for all students whose first name or last name contains "dan", I would type in dan in place of arg2; arg1 would be -name.
If I want to search for all students with "joe" in their email, I would type in joe in place of arg2; arg1 would be -email.

If arg1 was -gpa then arg2 sould be a float followed by an optional suffix of '+' or '-' that denotes whether to denote whether the search used a gpa floor or ceiling respectively. If no suffix is included, only students with gpa's equal to that entered as arg2 will be printed. 
For example, to search for all students with gpa's greater than or equal to 3.64, I would enter '3.64+' as arg2. If I only want students with gpa's equal to 3.5, I would enter '3.5' as arg2. 

arg3 should be the name of the csv file containing the roster in which the search is to be performed on. 

-----

If I want to search for all students with "dab" in either their first name or last name, and the roster has a file name of roster.csv, I would type this into the terminal:

py rostersearch.py -name dab roster.csv

-----

If I want to search for all students with "john" in their email, and the roster has a file name of classroster.csv, I would type this into the terminal:

py rostersearch.py -email john classroster.csv

-----

If I want to search for all students with a gpa less than or equal to 3.44, and the roster has a file name of mystudents.csv, I would type this into the terminal:

py rostersearch.py -gpa 3.44- mystudents.csv

-----

Description of each file:

README.md - Gives instructions on how to run the script as well as a description about the role of each file in the project.

example_roster.csv - An example of a csv file to show how to format the students. Notice how the first row is for column titles and the 4 columns are First Name, Last Name, Email, and GPA of students respectively. 

rostersearch.py - This is the file that starts running when the the script is executed.

rostertest.py - This filecontains the unit tests that I wrote to test the functions of search_commands.py. They were written using the unittest framework. 
To run the unit tests, type into the terminal: py rostertest.py

search_commands.py - This file contains the functions that perform the searches as well as the function that determines whether the user-entered GPA without the suffix is indeed a float.



