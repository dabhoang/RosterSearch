import sys
import csv
from search_commands import *

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
students = list(csv.reader(x.replace('\0', '') for x in roster)) #students is a list of all students

#determines the function for appropriate column(s) to search based on command
if sys.argv[1] == "-name": #command is “-name <pattern>”
    search_name(sys.argv[2], students)
elif sys.argv[1] == "-email": #command is “-email <pattern>”
    search_email(sys.argv[2], students)
elif sys.argv[1] == "-gpa": #command is “-gpa <gpa>[+-]”
    search_gpa(sys.argv[2], students)

else: print("Please enter -name -email or -gpa as the first command line argument after rostersearch.py") #first command line argument after rostersearch.py should be -name, -email, or -gpa

roster.close() #close the csv file