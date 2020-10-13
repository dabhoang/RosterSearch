from io import StringIO 
from unittest import TestCase 
from unittest.mock import patch 
import unittest
#import rostersearch_test
import sys
import csv
import search_commands

class TestRoster(TestCase):
    def test_name0(self): 
        people_in_class = list(csv.reader(roster)) #students is a list of all students
        expected = "Searching for all students with \"dab\" in their first name or last name:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_name("dab", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)

    def test_name1(self): 
        roster.truncate(0)
        writer = csv.writer(roster)
        rows_of_people = [["First Name", "Last Name", "Email", "GPA"], ["Dan", "Hoang", "danhoang@ucdavis.edu", 3.00]]
        writer.writerows(rows_of_people)
        people_in_class = list(csv.reader(roster))
        expected = "Searching for all students with \"dab\" in their first name or last name:\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_name("dab", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)

    def test_name2(self): 
        roster.truncate(0)
        writer = csv.writer(roster)
        rows_of_people = [["First Name", "Last Name", "Email", "GPA"], ["Dan", "Hoang", "danhoang@ucdavis.edu", "3.00"]]
        writer.writerows(rows_of_people)
        roster.close()
        nw_roster = open("roster.csv", 'r+', encoding = 'utf-8') #open the csv file
        people_in_class = list(csv.reader(x.replace('\0', '') for x in nw_roster))
        expected = "Searching for all students with \"a\" in their first name or last name:\n" + "[\'Dan\', \'Hoang\', \'danhoang@ucdavis.edu\', '3.00']\n"
        with patch('sys.stdout', new = StringIO()) as actual_results:
            search_commands.search_name("a", people_in_class)
            self.assertEqual(actual_results.getvalue(), expected)

   
            


#if __name__ == '__main__':
roster = open("roster.csv", 'w+', encoding = 'utf-8', newline="") #open the csv file

unittest.main()
roster.close()
nw_roster.close()












#f = open("result.csv",'w', encoding = 'utf-8')



#test the search_name() function

#test the search_email() function

#test the search_gpa() function

#test the check_gpa_is_float() function