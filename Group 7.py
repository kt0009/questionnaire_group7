# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Data Science: Group 7 

# <rawcell>

# Carl Shan, He Ma, Alyssa Parker, Vincent Canlas

# <headingcell level=2>

# Step 0: Setup

# <markdowncell>

# Import basic Python libraries for use in your program: [os.path](http://docs.python.org/2/library/os.path.html) and [ConfigParser](http://docs.python.org/2/library/configparser.html). We also imported re and csv for regular expression parsing and creating csv files respectively.

# <codecell>

import os.path
import ConfigParser
import re
import csv

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

# <headingcell level=2>

# Step 1 - Curation

# <headingcell level=3>

# Part A - Cleaning up Data

# <codecell>

def clean_classes(string):
    'This function cleans the list of classes, pruning it to just include the Stat 130s'
    s = []
    for elem in ('133', '134', '135'):
        if elem in string:
            s.append('STAT' + elem)
    return(s)

## Removing unicode from corpus
filtered_data[17][fieldnames[2]] = re.sub(u'\u2022', '', filtered_data[17][fieldnames[1]])
filtered_data[24][fieldnames[2]] = re.sub(u'\u2013', '', filtered_data[24][fieldnames[1]])

## Creates Cleaned Dictionary to be parsed into .csv
cleaned_data = []
for elem in filtered_data:
    if 'Kinesthetic' in elem[fieldnames[1]]: # checks to see if the cell is non-empty and machine readable
        scores = re.findall('\d+', elem[fieldnames[1]])
        row_dict = {'Timestamp' : elem['Timestamp'], 'Visual' : scores[0], 'Aural' : scores[1], 'Read_Write' : scores[2], 'Kinesthetic': scores[3], 'STAT133' : '0', 'STAT134' : '0', 'STAT135' : '0', 'CS' : '0'}
        classes = clean_classes(elem[fieldnames[2]]) # only keeps Stat 133, Stat 134 and Stat 135
        for course in ('STAT133', 'STAT134', 'STAT135'):
            if course in classes:
                row_dict[course] = 1
        if re.match(r'[Cc][Ss] ?[0-9]+',elem[fieldnames[2]]): # if the person has taken as CS classes
            row_dict['CS'] = 1
        cleaned_data.append(row_dict)

# <headingcell level=3>

# Part B - Creating .csv File

# <codecell>

## Creates a .csv file called data.csv from cleaned data
names = ['Timestamp', 'Aural', 'Kinesthetic', 'Read_Write', 'Visual', 'STAT133', 'STAT134', 'STAT135', 'CS']
f = open('data.csv', 'wb')
dict_writer = csv.DictWriter(f, names, restval='NA')
dict_writer.writeheader()
dict_writer.writerows(cleaned_data)

# <headingcell level=2>

# Step 2 - Analysis

# <codecell>

# code start here

# <headingcell level=2>

# Step3 - Visualization

# <rawcell>

# Everything is done with R, please refer to visulization.R for implementation.

# <headingcell level=3>

# Part A: Learning Style

# <headingcell level=4>

# Distribution of the scores for Aural, Kinesthetic, Read_Write, Visual

# <markdowncell>

# <img src="files/hist_style.png">
# <img src="files/violin_style.png">

# <rawcell>

# Due to the limitation of the size of the data, we can't really say much about the data. 
# Aural score spread out between 1 and 11, while the other three scores have a larger spread.
# Seems like the scores could fit with normal distribution.

# <headingcell level=4>

# Normal distribution fitness

# <markdowncell>

# <img src="files/normal_style.png">

# <rawcell>

# Since the data is ordinal, this plot can only be taken as a reference.
# Aural has big tail for both sides. 
# The other three are approximately normal, but skew to the side.

# <headingcell level=4>

# Pairsie correlation for learning style

# <markdowncell>

# <img src="~/files/scatterplot_style.png">

# <rawcell>

# All seems to be evenly spread out.

# <markdowncell>

# <img src="files/heatmap_style.png">

# <rawcell>

# Again, since the data is ordinal, Pearson's correlation might not be a accurate prediction.
# Still, we can see that Read_Write is not correlatied with the other three categories.
# For Aural, Kinesthetic, and Visual, if the student score higher in one of them, he is likely to score higher in the other two.

# <headingcell level=3>

# Part B: Classes taken

# <headingcell level=4>

# Distribution of people taking STAT and CS class

# <markdowncell>

# <img src="files/barplot_class.png">
# <img src="files/stat_cs_class.png">

# <rawcell>

# There might be some correlation between learning style and the different classes people take.
# But due to the limitation of the sample size, it is not likely we can get to a conclusion

