# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Import basic Python libraries for use in your program: [os.path](http://docs.python.org/2/library/os.path.html) and [ConfigParser](http://docs.python.org/2/library/configparser.html)

# <codecell>

import os.path
import ConfigParser

# <markdowncell>

# An example of reading data from a Google Spreadsheet using the gspread library: http://stackoverflow.com/a/18296318/462302
# 
# First you'll need to install the gspread library on your virtual machine using: `sudo pip install gspread`

# <codecell>

import gspread

# <markdowncell>

# Define `take(n, iterable)` which is a convenience function to limit the amount of output that you print. Useful when you have lots of data that will clutter up your screen!

# <codecell>

from itertools import islice
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

# <markdowncell>

# Read the username and password from the `[google]` section of the `stat157.cfg` config file from your virtual machine home directory.

# <codecell>

home = os.path.expanduser("~")
configfile = os.path.join(home, 'stat157.cfg')
config = ConfigParser.SafeConfigParser()
config.read(configfile)
username = config.get('google', 'username')
password = config.get('google', 'password')
print username

# <markdowncell>

# Read the docid of the Google Spreadsheet from the config file.

# <codecell>

docid = config.get('questionnaire', 'docid')
client = gspread.login(username, password)
spreadsheet = client.open_by_key(docid)
worksheet = spreadsheet.get_worksheet(0)
print docid

# <markdowncell>

# Add field names to this list to include the column from the Google Spreadsheet in the filtered data output. You should choose one other column in addition to the learning style column. Refer to README.md from the homework assignment.

# <codecell>

fieldnames = ['Timestamp','What is your learning style?', 'Which department and course numbers (e.g. Stat 157)?']
print fieldnames

# <markdowncell>

# Read in ALL rows of data from the Google Spreadsheet, but filter out columns that are not listed in `fieldnames`.

# <codecell>

filtered_data = []
for row in worksheet.get_all_records():
    filtered_data.append({k:v for k,v in row.iteritems() if k in fieldnames})
print "Number of rows: {}".format(len(filtered_data))

# <markdowncell>

# Use the convenience function `take()` to print out only 3 lines from the filtered_data.

# <codecell>

### Cleaning up filtered_data
import re
import csv

## Removing unicode
filtered_data[17][fieldnames[2]] = re.sub(u'\u2022', '', filtered_data[17][fieldnames[1]])
filtered_data[24][fieldnames[2]] = re.sub(u'\u2013', '', filtered_data[24][fieldnames[1]])

def clean_classes(string):
	s = []
	for elem in ('133', '134', '135'):
		if elem in string:
			s.append('Stat ' + elem)
	return(s)

## Creates Cleaned Dictionary to be parsed into .csv
cleaned_data = []
for elem in filtered_data:
	if 'Kinesthetic' in elem[fieldnames[1]]: # checks to see if the cell is non-empty and machine readable
		scores = re.findall('\d+', elem[fieldnames[1]])
		row_dict = {'Timestamp' : elem['Timestamp'], 'Visual' : scores[0], 'Aural' : scores[1], 'Read/Write' : scores[2], 'Kinesthetic': scores[3], 'Stat 133' : '0', 'Stat 134' : '0', 'Stat 135' : '0'}
		classes = clean_classes(elem[fieldnames[2]]) # only keeps Stat 133, Stat 134 and Stat 135
		for elem in ('Stat 133', 'Stat 134', 'Stat 135'):
			if elem in classes:
				row_dict[elem] = 1
		cleaned_data.append(row_dict)

# Creates .csv file with cleaned data
names = ['Timestamp', 'Aural', 'Kinesthetic', 'Read/Write', 'Visual', 'Stat 133', 'Stat 134', 'Stat 135']
f = open('data.csv', 'wb')
dict_writer = csv.DictWriter(f, names, restval='NA')
dict_writer.writeheader()
dict_writer.writerows(cleaned_data)

