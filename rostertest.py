from io import StringIO 
from unittest import TestCase 
from unittest.mock import patch 
import unittest
#import rostersearch_test
import sys
import csv
import search_commands

class TestRoster(TestCase):

    #test the search_name() function

    def test_search_name_empty_file(self): 
        expected = "Searching for all students with \"dab\" in their first name or last name:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_name("dab", people_empty)
            self.assertEqual(actual_results.getvalue(), expected)

    def test_search_name_empty_roster_with_column_titles(self): 
        expected = "Searching for all students with \"irs\" in their first name or last name:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_name("irs", people_columns_only)
            self.assertEqual(actual_results.getvalue(), expected)
        
    def test_search_name_roster_size_1_with_no_students_printed(self): 
        expected = "Searching for all students with \"dab\" in their first name or last name:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_name("dab", people_size_1)
            self.assertEqual(actual_results.getvalue(), expected)
        
    def test_search_name_roster_size_1_with_1_student_printed(self): 
        read_roster = open("roster_size_1.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching for all students with \"a\" in their first name or last name:\n" + "[\'Dan\', \'Hoang\', \'danhoang@ucdavis.edu\', '3.0']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_name("a", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    def test_name_roster_size_5_with_some_students_printed_lowercase_pattern(self): 
        read_roster = open("roster_size_5.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching for all students with \"jo\" in their first name or last name:\n" 
        expected = expected + "[\'John\', \'Smith\', \'jsmith@ucdavis.edu\', '3.78']\n"
        expected = expected + "[\'Joey\', \'Johnson\', \'jjohnson@ucdavis.edu\', '2.2']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_name("jo", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    def test_name_roster_size_5_with_some_students_printed_uppercase_pattern(self): 
        read_roster = open("roster_size_5.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching for all students with \"Jo\" in their first name or last name:\n" 
        expected = expected + "[\'John\', \'Smith\', \'jsmith@ucdavis.edu\', '3.78']\n"
        expected = expected + "[\'Joey\', \'Johnson\', \'jjohnson@ucdavis.edu\', '2.2']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_name("Jo", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    #--------------------------------------
    #test the search_email() function

    def test_search_email_empty_roster(self): 
        expected = "Searching for all students with \"dab\" in their email without the \"@ucdavis.edu\" suffix:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_email("dab", people_empty)
            self.assertEqual(actual_results.getvalue(), expected)

    def test_search_email_roster_size_1_with_no_students_printed(self): 
        expected = "Searching for all students with \"dab\" in their email without the \"@ucdavis.edu\" suffix:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_email("dab", people_size_1)
            self.assertEqual(actual_results.getvalue(), expected)

    def test_search_email_roster_size_1_with_1_student_printed(self): 
        read_roster = open("roster_size_1.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching for all students with \"a\" in their email without the \"@ucdavis.edu\" suffix:\n" + "[\'Dan\', \'Hoang\', \'danhoang@ucdavis.edu\', '3.0']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_email("a", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    def test_search_email_roster_size_5_lowercase_pattern(self): 
        
        read_roster = open("roster_size_5.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching for all students with \"jo\" in their email without the \"@ucdavis.edu\" suffix:\n" 
        expected = expected + "[\'Joey\', \'Johnson\', \'jjohnson@ucdavis.edu\', '2.2']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_email("jo", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    def test_search_email_roster_size_5_uppercase_pattern(self): 
        read_roster = open("roster_size_5.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching for all students with \"JO\" in their email without the \"@ucdavis.edu\" suffix:\n" 
        expected = expected + "[\'Joey\', \'Johnson\', \'jjohnson@ucdavis.edu\', '2.2']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_email("JO", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    def test_search_email_roster_size_5_pattern_appears_in_suffix(self): 
        read_roster = open("roster_size_5.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching for all students with \"davi\" in their email without the \"@ucdavis.edu\" suffix:\n" 
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_email("davi", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    #--------------------------------------
    #test the check_gpa_is_float() function
    def test_check_gpa_is_float_with_invalid_gpa(self): 
        
        expected = "Please enter gpa in the form of a float followed by an optional suffix of \'+\' or \'-\'\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.check_gpa_is_float("dab")
            self.assertEqual(actual_results.getvalue(), expected)
    
    def test_check_gpa_is_float_with_valid_gpa(self): 
        expected = ""
        with patch('sys.stdout', new = StringIO()) as actual_result:
            search_commands.check_gpa_is_float("3.2")
            self.assertEqual(actual_result.getvalue(), expected)

    #--------------------------------------
    #test the search_gpa() function
    def test_search_gpa_with_invalid_gpa(self): 
        expected = "Please enter gpa in the form of a float followed by an optional suffix of \'+\' or \'-\'\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_gpa("dab" , people_empty)
            self.assertEqual(actual_results.getvalue(), expected)   

    def test_search_gpa_empty_roster(self): 
        expected = "Searching roster for students with a gpa of 3.2:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_gpa("3.2" , people_empty)
            self.assertEqual(actual_results.getvalue(), expected)

    def test_search_gpa_roster_size_1_with_no_students_printed_floor(self): 
        expected = "Searching roster for students with a gpa of 3.2 and above:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_gpa("3.2+", people_size_1)
            self.assertEqual(actual_results.getvalue(), expected)

    def test_search_gpa_roster_size_1_with_no_students_printed_ceiling(self): 
        expected = "Searching roster for students with a gpa of 2.8 and below:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_gpa("2.8-", people_size_1)
            self.assertEqual(actual_results.getvalue(), expected)

    def test_search_gpa_roster_size_1_with_1_student_printed_ceiling(self): 
        read_roster = open("roster_size_1.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching roster for students with a gpa of 3.2 and below:\n" + "[\'Dan\', \'Hoang\', \'danhoang@ucdavis.edu\', '3.0']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_gpa("3.2-", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    def test_search_gpa_roster_size_1_with_1_student_printed_floor(self): 
        read_roster = open("roster_size_1.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching roster for students with a gpa of 2.8 and above:\n" + "[\'Dan\', \'Hoang\', \'danhoang@ucdavis.edu\', '3.0']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_gpa("2.8+", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    def test_search_gpa_roster_size_12_with_some_students_printed_equals(self): 
        read_roster = open("roster_size_12.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching roster for students with a gpa of 3.0:\n" 
        expected = expected + "[\'Dan\', \'Hoang\', \'danhoang@ucdavis.edu\', \'3.0\']\n"
        expected = expected + "[\'David\', \'Davidson\', \'ddavidson@ucdavis.edu\', \'3.0\']\n"
        expected = expected + "[\'Larry\', \'Larson\', \'llarson@ucdavis.edu\', \'3.0\']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_gpa("3.0", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()




#if __name__ == '__main__':
roster_empty = open("roster_empty.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
people_empty = list(csv.reader(roster_empty)) #students is a list of all students
roster_empty.close()


roster_column_titles_only = open("roster_titles_only.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
roster_column_titles_only.truncate(0)
writer = csv.writer(roster_column_titles_only)
writer.writerow(["First Name", "Last Name", "Email", "GPA"])
people_columns_only = list(csv.reader(roster_column_titles_only))
roster_column_titles_only.close()


roster_size_1 = open("roster_size_1.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
roster_size_1.truncate(0)
writer = csv.writer(roster_size_1)
writer.writerow(["First Name", "Last Name", "Email", "GPA"])
writer.writerow(["Dan", "Hoang", "danhoang@ucdavis.edu", '3.0'])
people_size_1 = list(csv.reader(roster_size_1))
roster_size_1.close()

roster_size_5 = open("roster_size_5.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
roster_size_5.truncate(0)
writer = csv.writer(roster_size_5)
writer.writerow(["First Name", "Last Name", "Email", "GPA"])
writer.writerow(["Dan", "Hoang", "danhoang@ucdavis.edu", "3.0"])
writer.writerow(["John", "Smith", "jsmith@ucdavis.edu", "3.78"])
writer.writerow(["Joey", "Johnson", "jjohnson@ucdavis.edu", "2.2"])
writer.writerow(["Eddie", "Jacobs", "ejacobs4@ucdavis.edu", "4.0"])
writer.writerow(["Jimmy", "Graham", "jgraham@ucdavis.edu", "3.22"])
roster_size_5.close()

roster_size_12 = open("roster_size_12.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
roster_size_12.truncate(0)
writer = csv.writer(roster_size_12)
writer.writerow(["First Name", "Last Name", "Email", "GPA"])
writer.writerow(["Dan", "Hoang", "danhoang@ucdavis.edu", "3.0"])
writer.writerow(["John", "Smith", "jsmith@ucdavis.edu", "3.78"])
writer.writerow(["Joey", "Johnson", "jjohnson@ucdavis.edu", "2.2"])
writer.writerow(["Eddie", "Jacobs", "ejacobs4@ucdavis.edu", "4.0"])
writer.writerow(["Jimmy", "Graham", "jgraham@ucdavis.edu", "3.22"])
writer.writerow(["David", "Davidson", "ddavidson@ucdavis.edu", "3.0"])
writer.writerow(["Peter", "Peterson", "ppeterson@ucdavis.edu", "1.5"])
writer.writerow(["John", "Johnson", "jjohnson2@ucdavis.edu", "3.5"])
writer.writerow(["Jack", "Jackson", "jjackson@ucdavis.edu", "2.4"])
writer.writerow(["Ed", "Edison", "eedison@ucdavis.edu", "2.7"])
writer.writerow(["Harry", "Harrison", "hharrison@ucdavis.edu", "2.9"])
writer.writerow(["Larry", "Larson", "llarson@ucdavis.edu", "3.0"])
roster_size_12.close()


unittest.main()
#roster.close()


#f = open("result.csv",'w', encoding = 'utf-8')

