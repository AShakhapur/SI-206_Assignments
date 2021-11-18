# SI 206
# HW6 - Regular Expressions
# Name: Abhay Shakhapur
# Who did you work with:　

import re
import os
import unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """

    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')

    # Read the lines from the file object into a list
    lines = infile.readlines()

    # Close the file object
    infile.close()

    # return the list of lines
    return lines


def find_time(string_list):
    """ Return a list of valid times from the list of strings.
        string_list -- the name of the file to read from
        return -- the list of all times from a list of strings
    """
    lines =read_file(string_list)
    times = []
    times2 = []
    edited_times = []
    for x in lines:
        if re.search('[0-9]{1,2}:[0-9]{2}\s(am|pm)', x):
            times.append(re.findall(r'(([01]?[0-9]):([0-5][0-9]) ([AaPp][Mm]))', x))
    for x in times:
        times2.append(x[0])
    for x in times2:
        edited_times.append(x[0])
    #print(edited_times)
    return edited_times

def find_urls(string_list):

    """ Return a list of valid urls in the list of strings """
    lines =read_file(string_list)
    urls = []
    edited_urls = []
    yes = []
    for x in lines:
        if re.search('(?P<url>https?://[^\s]+)', x):
            #print('yes')
            yes.append(True)
            urls.append(re.findall(r'(?P<url>https?://[^\s]+)', x))
    for x in urls:
        edited_urls.append(x[0])
    #print(edited_urls)
    return edited_urls

def find_dates(string_list):
    """ Return a list of dates in the list of strings """
    lines =read_file(string_list)
    dates = []
    edited_dates = []
    yes = []
    for x in lines:
        if re.search('([0-2][0-9]|(3)[0-1])[-|\/](((0)[0-9])|((1)[0-2]))[-|\/]\d{4}', x):
            yes.append(True)
    print(yes)   

def find_underscore(string_list):
    """returns a list of words containted in underscores like _example_ """
    lines =read_file(string_list)
    list1 = []
    for line in lines:
        for word in line.split():
            if word.startswith("_") and word.endswith("_"):
                list1.append(word)
    return list1
find_underscore("alice_in_wonderland.txt")

## Extra credit
def count_char(string_list, char):
    """  return a count of the number of times a specified character appears in a list of strings.
        It should match the character when it starts or ends a word
        (It should not match any characters in the middle of a word)

        string_list -- the list of strings to count the char in
        char -- the character to look for
        return -- a count of the number of times the word or its plural appears in the file
    """
    lines =read_file(string_list)

    pass


# Implement your own tests.
class TestAllMethods(unittest.TestCase):


    def test_find_times(self):
        pass

    def test_find_urls(self):

        pass

    def test_find_dates(self):

        pass


    def test_find_underscore(self):

        pass

    def test_count_char(self):

        pass



def main():
	# Use main to test your function.
    # Run unit tests, but feel free to run any additional functions you need
	unittest.main(verbosity = 2)
if __name__ == "__main__":
	main()