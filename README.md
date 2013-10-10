Stat 157 Questionnaire Data Wrangling
=====================================

Group Members:
--------------
Vincent Canlas, He Ma, Alyssa Parker, Carl Shan

How to reproduce the data:
---------------------------
1. [Group7.ipynb](https://github.com/sunnymh/questionnaire_group7/blob/master/Group%207.ipynb) is the file containing our final product.  
Step0 and step 1 contain the code for pasing the data, which produces [data.csv](https://github.com/sunnymh/questionnaire_group7/blob/master/data.csv), and step 2 and 3 are the results of analysis and visualization in R.  
In order for everything show up in ipython notebook, run step 0 and 1 of the file. Run [visualization.R](https://github.com/sunnymh/questionnaire_group7/blob/master/visualization.R), then run step 2 and 3 in this file.  
Import basic Python libraries for use in your program: [os.path](http://docs.python.org/2/library/os.path.html) and [ConfigParser](http://docs.python.org/2/library/configparser.html).  
We also imported `re` and `csv` for regular expression parsing and creating csv files respectively.  
Make sure you have all the plots in the same directory in order for the plots to be shown in the notebook.  
2. [Questionnaire_ttests.R](https://github.com/sunnymh/questionnaire_group7/blob/master/Questionnaire_ttests.R) is the R code for analysis.  
If you want to reproduce the data, please add the directory which contains the project to `dir = ` in the first line of the code before running it. It will read in [data.csv](https://github.com/sunnymh/questionnaire_group7/blob/master/data.csv) produced by [Group7.ipynb](https://github.com/sunnymh/questionnaire_group7/blob/master/Group%207.ipynb)   
3. [visualization.R](https://github.com/sunnymh/questionnaire_group7/blob/master/visualization.R) is the R code for visualization.  
If you want to reproduce the data, please add the directory which contains the project to `dir = ` in the first line of the code. It will read in [data.csv](https://github.com/sunnymh/questionnaire_group7/blob/master/data.csv) produced by [Group7.ipynb](https://github.com/sunnymh/questionnaire_group7/blob/master/Group%207.ipynb) and produce the plots in the directory.  
It uses [vioplot](http://cran.r-project.org/web/packages/vioplot/index.html), [pheatmap](http://cran.r-project.org/web/packages/pheatmap/index.html) and [plotrix](http://cran.r-project.org/web/packages/plotrix/index.html). Please install these three packages before running the code.




Due Date
--------
This assignment is due on Monday, Oct 7th by 11:59pm.

The following day (Tuesday) in class you will present your work.

Turn in your homework with a final `git push` of all materials by the
deadline noted above.

Your presentations will be alloted no more than 3 minutes and you will
*not* present using your own laptop. Your presentation must be in a
form that can be displayed on your instructor's system in an open
format: either the IPython Notebook or an HTML5-based presentation is
preferred: <https://www.google.com/search?q=html5+presentations>.


Objective
---------

You will use the Stat 157 Questionnaire data that you will access
using the Google API. Your primary objective is to visualize data from
two columns of the spreadsheet data: 1) the column labeled "What is
your learning style?" and 2) any other column of your choosing that
you feel helps give us insight into the people in the class. [Question
and clarification](https://github.com/stat157/questionnaire/issues/2).

The data that we have available in the spreadsheet comes from the real
world, which means the data is **dirty**. Your job before you
visualize the data is to clean it up and transform it into a form that
the analyzers and visualizers in your group can use.

Specifically, this is the data that YOU submitted via the Google Form
as part of the Questionnaire for this course so we can better
understand you, your skills, and where you're headed after you
graduate. All identifying data has been redacted from this data!


The Data
--------

The data you use comes from this redacted Google Spreadsheet adapted
from the Questionnaire you filled out:

http://goo.gl/Cplm9O

The document has been shared with your @berkeley.edu account **ONLY**
and you must use your bConnected key to access it. You should make
sure you can open the above link in your browser to verify you can
access the document with your account.

NOTE: Do **NOT** simply copy & paste or export a CSV file from the
document. You must use the provided example IPython Notebook to start
with to access the data via the Google API.


Grading
-------

You will be graded based on both **the product AND the process** of
your veritcal (4 person) groups.

We will be able to see what you produce, so examining your end product
will be our method of determing the portion of your grade based on the
end-product itself.

The other portion of your grade will depend on the process of how you
arrived at your end-product. **Your process MUST be reproducible by
someone else *without* further instructions or help from you.** If you
cannot fully automate the process, then provide step-by-step
instructions.


QUESTIONS?!?!?!?!
-----------------
You will probably have a lot of questions. You may also find a few
bugs. Please use the Github Issue Tracker for this repository to ask
questions and submit bugs:

https://github.com/stat157/questionnaire/issues


Preliminary Setup Steps
-----------------------
You'll need to follow these steps on your virtual machine to do data
wrangling for this assignment:

    sudo apt-get install ipython ipython-notebook python-pip
    sudo pip install gspread

Then copy the example config file to your home directory, but named
`stat157.cfg` like this:

    cp example.cfg ~/stat157.cfg

Use a programming text editor to edit the example config file
`~/stat157.cfg` such as:

    vi ~/stat157.cfg

Edit the `~/stat157.cfg` config file so it will use your full
@berkeley username, e.g.: `foobear@berkeley.edu`. The password should
be your [bConnected key](https://kb.berkeley.edu/campus-shared-services/page.php?id=27226).

NOTE: Do **NOT** put your actual password into example.cfg! And
definitely **DO NOT** check it into github!

**UPDATE:** You might also be wondering [How to save your edit in vi](https://github.com/stat157/questionnaire/issues/3).

Use `example.ipynb` in this repository as a starting point to access
the Google Spreadsheet data. You should run the IPython Notebook in
your virtual machine using this command:

    ipython notebook --no-browser --ip=0.0.0.0

You can auto-generate a .py file from your IPython Notebook using an
additional argument:

    ipython notebook --no-browser --ip=0.0.0.0 --script

Sometimes it is convenient to easily track changes between versions of
your script by checking in changes made to the script in git since the
IPython Notebook is hard to inspect using a text editor instead of a
browser.

Hints For Success
-----------------
To be successful you will need to collaborate within your horizontal
(11 person) AND vertical (4 person) groups.

You have a better chance of succeeding with this assignment by running
`git commit` frequently on your local system and by running `git push`
often. If you're not sure what this means or have any questions, use
resources such as GitHub Help, StackOverflow, IRC, and other
resources that we configured in the first weeks of the class.

Keep notes about your process. If you are not able to make your
process reproducible by the deadline then you should be able to
provide notes about the errors, confusions, and other roadblocks that
you encountered.

Also, keep track of those "Aha!" moments and share those with others
in the class.
