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
filtered_data[17] = {'Timestamp': '9/4/2013 23:16:01',
 'What is your learning style?': u'Your scores were:\nVisual: 10\nAural: 10\nRead/Write: 2\nKinesthetic: 13\n\n You have a multimodal (VAK) learning preference.\n\n\n \n ',
 'Which department and course numbers (e.g. Stat 157)?': ''}

filtered_data[24] = {'Timestamp': '9/5/2013 0:30:46',
  'What is your learning style?': u"You are helping someone who wants to go to your airport, the center of town or railway station. You would:\nwrite down the directions.\ndraw, or show her a map, or give her a map.\n\nYou have finished a competition or test and would like some feedback. You would like to have feedback:\nusing examples from what you have done.\nfrom somebody who talks it through with you.\nusing a written description of your results.\n\nYou want to learn a new program, skill or game on a computer. You would:\ntalk with people who know about the program.\nuse the controls or keyboard.\nfollow the diagrams in the book that came with it.\n\nI like websites that have:\nthings I can click on, shift or try.\ninteresting written descriptions, lists and explanations.\ninteresting design and visual features.\n\nYou are planning a vacation for a group. You want some feedback from them about the plan. You would:\ndescribe some of the highlights they will experience.\nphone, text or email them.\n\nYou are not sure whether a word should be spelled `dependent' or `dependant'. You would:\nfind it online or in a dictionary.\n\nYou are going to cook something as a special treat. You would:\ncook something you know without the need for instructions.\nlook on the Internet or in some cookbooks for ideas from the pictures.\n\nYou are going to choose food at a restaurant or cafe. You would:\nchoose from the descriptions in the menu.\nlisten to the waiter or ask friends to recommend choices.\nchoose something that you have had there before.\n\nYou have a problem with your heart. You would prefer that the doctor:\nused a plastic model to show what was wrong.\ngave you something to read to explain what was wrong.\ndescribed what was wrong.\n\nRemember a time when you learned how to do something new. Avoid choosing a physical skill, eg. riding a bike. You learned best by:\nwatching a demonstration.\nwritten instructions e.g. a manual or book.\nlistening to somebody explaining it and asking questions.\n\nOther than price, what would most influence your decision to buy a new non-fiction book?\nA friend talks about it and recommends it.\n\nYou are using a book, CD or website to learn how to take photos with your new digital camera. You would like to have:\nclear written instructions with lists and bullet points about what to do.\ndiagrams showing the camera and what each part does.\n\nYou are about to purchase a digital camera or mobile phone. Other than price, what would most influence your decision?\nTrying or testing it\nReading the details or checking its features online.\n\nDo you prefer a teacher or a presenter who uses:\ndemonstrations, models or practical sessions.\nquestion and answer, talk, group discussion, or guest speakers.\ndiagrams, charts or graphs.\n\nA group of tourists wants to learn about the parks or wildlife reserves in your area. You would:\ntalk about, or arrange a talk for them about parks or wildlife reserves.\ntake them to a park or wildlife reserve and walk with them.\n\nYou have to make an important speech at a conference or special occasion. You would:\nwrite a few key words and practice saying your speech over and over.\nwrite out your speech and learn from reading it over several times.\n",
  'Which department and course numbers (e.g. Stat 157)?': 'CS61A, CS61B, stat133,stat 134, stat135'}

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

names = ['Timestamp', 'Aural', 'Kinesthetic', 'Read/Write', 'Visual', 'Stat 133', 'Stat 134', 'Stat 135']


# Creates .csv file with cleaned data
f = open('data.csv', 'wb')
dict_writer = csv.DictWriter(f, names, restval='NA')
dict_writer.writeheader()
dict_writer.writerows(cleaned_data)

