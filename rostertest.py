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

    def test_name0(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        people_in_class = list(csv.reader(roster)) #students is a list of all students
        expected = "Searching for all students with \"dab\" in their first name or last name:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_name("dab", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        roster.close()

    def test_name1(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        roster.truncate(0)
        writer = csv.writer(roster)
        writer.writerow(["First Name", "Last Name", "Email", "GPA"])
        writer.writerow(["Dan", "Hoang", "danhoang@ucdavis.edu", '3.0'])
        people_in_class = list(csv.reader(roster))
        expected = "Searching for all students with \"dab\" in their first name or last name:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_name("dab", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        roster.close()
        

    def test_name2(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        roster.truncate(0)
        writer = csv.writer(roster)
        writer.writerow(["First Name", "Last Name", "Email", "GPA"])
        writer.writerow(["Dan", "Hoang", "danhoang@ucdavis.edu", "3.0"])
        roster.close()
        read_roster = open("roster.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching for all students with \"a\" in their first name or last name:\n" + "[\'Dan\', \'Hoang\', \'danhoang@ucdavis.edu\', '3.0']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_name("a", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    def test_name3(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        roster.truncate(0)
        writer = csv.writer(roster)
        writer.writerow(["First Name", "Last Name", "Email", "GPA"])
        writer.writerow(["Dan", "Hoang", "danhoang@ucdavis.edu", "3.0"])
        writer.writerow(["John", "Smith", "jsmith@ucdavis.edu", "3.78"])
        writer.writerow(["Joey", "Johnson", "jjohnson@ucdavis.edu", "2.2"])
        writer.writerow(["Eddie", "Jacobs", "ejacobs4@ucdavis.edu", "4.0"])
        writer.writerow(["Jimmy", "Graham", "jgraham@ucdavis.edu", "3.22"])
        roster.close()
        read_roster = open("roster.csv", 'r+', encoding = 'utf-8') #open the csv file
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

    def test_email0(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        people_in_class = list(csv.reader(roster)) #students is a list of all students
        expected = "Searching for all students with \"dab\" in their email without the \"@ucdavis.edu\" suffix:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_email("dab", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        roster.close()

    def test_email1(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        roster.truncate(0)
        writer = csv.writer(roster)
        writer.writerow(["First Name", "Last Name", "Email", "GPA"])
        writer.writerow(["Dan", "Hoang", "danhoang@ucdavis.edu", '3.0'])
        people_in_class = list(csv.reader(roster))
        expected = "Searching for all students with \"dab\" in their email without the \"@ucdavis.edu\" suffix:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_email("dab", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        roster.close()

    def test_email2(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        roster.truncate(0)
        writer = csv.writer(roster)
        writer.writerow(["First Name", "Last Name", "Email", "GPA"])
        writer.writerow(["Dan", "Hoang", "danhoang@ucdavis.edu", "3.0"])
        roster.close()
        read_roster = open("roster.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching for all students with \"a\" in their email without the \"@ucdavis.edu\" suffix:\n" + "[\'Dan\', \'Hoang\', \'danhoang@ucdavis.edu\', '3.0']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_email("a", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    def test_email3(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        roster.truncate(0)
        writer = csv.writer(roster)
        writer.writerow(["First Name", "Last Name", "Email", "GPA"])
        writer.writerow(["Dan", "Hoang", "danhoang@ucdavis.edu", "3.0"])
        writer.writerow(["John", "Smith", "jsmith@ucdavis.edu", "3.78"])
        writer.writerow(["Joey", "Johnson", "jjohnson@ucdavis.edu", "2.2"])
        writer.writerow(["Eddie", "Jacobs", "ejacobs4@ucdavis.edu", "4.0"])
        writer.writerow(["Jimmy", "Graham", "jgraham@ucdavis.edu", "3.22"])
        roster.close()
        read_roster = open("roster.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching for all students with \"jo\" in their email without the \"@ucdavis.edu\" suffix:\n" 
        expected = expected + "[\'Joey\', \'Johnson\', \'jjohnson@ucdavis.edu\', '2.2']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_email("jo", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    #--------------------------------------
    #test the search_gpa() function
    def test_gpa0(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        people_in_class = list(csv.reader(roster)) #students is a list of all students
        expected = "Searching roster for students with a gpa of 3.2:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_gpa("3.2" , people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        roster.close()

    def test_gpa1(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        roster.truncate(0)
        writer = csv.writer(roster)
        writer.writerow(["First Name", "Last Name", "Email", "GPA"])
        writer.writerow(["Dan", "Hoang", "danhoang@ucdavis.edu", '3.0'])
        people_in_class = list(csv.reader(roster))
        expected = "Searching roster for students with a gpa of 3.2 and above:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_gpa("3.2+", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        roster.close()

    def test_gpa2(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        roster.truncate(0)
        writer = csv.writer(roster)
        writer.writerow(["First Name", "Last Name", "Email", "GPA"])
        writer.writerow(["Dan", "Hoang", "danhoang@ucdavis.edu", "3.0"])
        roster.close()
        read_roster = open("roster.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching roster for students with a gpa of 3.2 and below:\n" + "[\'Dan\', \'Hoang\', \'danhoang@ucdavis.edu\', '3.0']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_gpa("3.2-", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()

    def test_gpa3(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        roster.truncate(0)
        writer = csv.writer(roster)
        writer.writerow(["First Name", "Last Name", "Email", "GPA"])
        writer.writerow(["Dan", "Hoang", "danhoang@ucdavis.edu", "3.0"])
        writer.writerow(["John", "Smith", "jsmith@ucdavis.edu", "3.78"])
        writer.writerow(["Joey", "Johnson", "jjohnson@ucdavis.edu", "2.2"])
        writer.writerow(["Eddie", "Jacobs", "ejacobs4@ucdavis.edu", "4.0"])
        writer.writerow(["Jimmy", "Graham", "jgraham@ucdavis.edu", "3.22"])
        roster.close()
        read_roster = open("roster.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in read_roster))
        expected = "Searching roster for students with a gpa of 2.2:\n" 
        expected = expected + "[\'Joey\', \'Johnson\', \'jjohnson@ucdavis.edu\', '2.2']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_gpa("2.2", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)
        read_roster.close()
        roster.close()

    def test_invalid_search_gpa(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        people_in_class = list(csv.reader(roster)) #students is a list of all students
        #self.assertRaises(ValueError, search_commands.check_gpa_is_float, "dab")
        expected = "Please enter gpa in the form of a float followed by an optional suffix of \'+\' or \'-\'\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_gpa("dab" , people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)   
        roster.close()

    #--------------------------------------
    #test the check_gpa_is_float() function
    def test_invalid_check_gpa_is_float(self): 
        roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file
        expected = "Please enter gpa in the form of a float followed by an optional suffix of \'+\' or \'-\'\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.check_gpa_is_float("dab")
            self.assertEqual(actual_results.getvalue(), expected)
        roster.close()

    
    def test_check_valid_check_gpa_is_float(self): 
        expected = ""
        with patch('sys.stdout', new = StringIO()) as actual_result:
            search_commands.check_gpa_is_float("3.2")
            self.assertEqual(actual_result.getvalue(), expected)

    


    
        
    #def test__check_gpa1(self): 
    #    roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="")
    #    expected = "Please enter gpa in the form of a float followed by an optional suffix of \'+\' or \'-\'"
    #    with patch('sys.stdout', new = StringIO()) as actual_result:
    #        search_commands.check_gpa_is_float("dab")
    #        self.assertEqual(actual_result.getvalue(), expected)


#if __name__ == '__main__':


unittest.main()
#roster.close()













#f = open("result.csv",'w', encoding = 'utf-8')

