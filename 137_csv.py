"""
CSV file (Comma Separated Values file)
- data are arranged in tabular format
- and separated by comma
- In general, the separator character is called a delimiter, 
  and the comma is not the only one used. (Other popular delimiters include the tab (\t), colon (:) and semi-colon (;))

- We can work on CSV data either with csv built in module or pandas library
"""

"""
Reading CSV file - with csv module

- The CSV file is opened as a text file with Python's built-in open() function, which returns a file object.
- This is then passed to the reader(),
"""
import csv

with open("emp_bd.txt", "r") as f:
    csv_reader = csv.reader(f, delimiter=",")
    line_count=0
    for each_row in csv_reader:
        # we are gonna get a list of each row
        print(each_row)
print()
# Reading CSV Files Into a Dictionary With csv
# Rather than deal with a list - we can directly read into Dict

with open("emp_bd.txt", "r") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        # we gonna get each row with Column - row pair in dict
        # The first line of the CSV file is assumed to contain the keys to use to build the dictionary.
        print(row)

print()
"""
Optional Python CSV reader Params -
- delimiter: specifies the character used to separate each field - the default is comma (',')
- quotechar: specifies the character used to surround fields that contain the delimiter character.
             The default is a double quote (' " ').
- escapechar: specifies the character used to escape the delimiter character, 
              in case quotes aren't used. The default is no escape character.
"""
# emp_add.txt = This txt file contains three fields: name, address, and date joined, 
#               which are delimited(having fixed boundaries) by commas. 
#               The problem is that the data for the address field also contains a comma 
#               to signify the zip code.

"""
For above Issue we can handle above with 3 different ways:

1. Use a different delimeter
2. Wrap the data in quotes
3. Escape the delimiter characters in the data
"""
print()
print("READING empd_add_bad.txt")
with open("emp_add_bad.txt", "r") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        print(i)
# Above is issue we can see in print statements 
"""
The csv module does not automatically handle commas within fields, 
so you'll have to preprocess your data to ensure the fields are correctly quoted.
- so either manually either below -
    name,address,date joined
    john smith,1132 Anywhere Lane Hoboken NJ, 07030,Jan 4
    erica meyers,1234 Smith Lane Hoboken NJ, 07030,March 2
into this -
    name,address,date joined
    "john smith","1132 Anywhere Lane Hoboken NJ, 07030","Jan 4"
    "erica meyers","1234 Smith Lane Hoboken NJ, 07030","March 2"

- or write a program that does apply "" to each column



"""
# Reading that file which has "" in their value
print()
print("READING empd_add_good.txt")
with open("emp_add_good.txt", "r") as f:
    csvreader = csv.reader(f, quotechar='"')
    for row in csvreader:
        print(row)

print()
# PANDAS
"""
pandas can automatically handle fields with commas if they are properly quoted. 
We can specify the quoting behavior when reading the CSV
"""

import pandas as pd

df = pd.read_csv('emp_add_bad.txt', quoting=csv.QUOTE_ALL)
print(df)

print()
# Writing CSV file
# in csv module we have .writer and .write_row method

with open('new_employee_file.csv', mode='w') as employee_file:
    # below are default parameters
    headers = ['Name', 'Occupation', 'Date']

    data = [
        ['Ash Porwal', 'Developer', 'July2022'],
        ['test sample', 'idk', 'March 2']
    ]

    employee_writer = csv.writer(
        employee_file, 
        delimiter=',', 
        quotechar='"', 
        quoting=csv.QUOTE_MINIMAL
        )

    # write header
    employee_writer.writerow(headers)

    # write rest rows
    for row in data:
        employee_writer.writerow(row)
print("created new_employee_file.csv file locally")

# Writing from a dict
with open('new_employee_file.csv', mode='w') as csv_file:
    headers = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(
        csv_file, 
        fieldnames=headers # passing headers
        )

    writer.writeheader()
    writer.writerow({'emp_name': 'Ash Porwal', 'dept': 'Developer', 'birth_month': 'August'})
    writer.writerow({'emp_name': 'test2', 'dept': 'IT', 'birth_month': 'March'})