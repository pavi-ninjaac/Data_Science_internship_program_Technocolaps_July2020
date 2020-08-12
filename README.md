# Data Science internship program Technocolaps July2020-Aug 2020
This is my journey fo data science internship at technocolaps. Here i am going to write the day by day activities of this internship and write about my assignments and projects and learing path.
# Day 1:
https://shahyaseen71.gitbook.io/data-science-internship/learn-from-the-basic-to-advanced
##### learning about what is data science and some importance of basic level:
# 2. What is Data Science?
Before we start the Data Science Tutorial, we should find out what data science really is.
Data science is a way to try and discover hidden patterns in raw data. To achieve this goal, it makes use of several algorithms, machine learning(ML) principles, and scientific methods. The insights it retrieves from data lie in forms structured and unstructured. So in a way, this is like data mining. Data science encompasses all- data analysis, statistics, and machine learning. With more practices being labelled into data science, the term itself becomes diluted beyond usefulness. This leads to variation in curricula for introductory data science courses worldwide.
# data science history:
In 90’s
- 1960- Peter Naur uses the term as a substitute for computer science.
- 1974- Peter Naur publishes Concise Survey of Computer Methods, uses a term in a survey of contemporary data processing methods.
- 1996- Biennial conference in Kobe; members of the IFCS (International Federation of Classification Societies include the term in the conference title.
- 1997- November- Professor C.F. Jeff Wu delivers inaugural lecture on the topic “Statistics=Data Science?”.
b. In 2000’s
- 2001- William S. Cleveland introduces data science as an independent discipline in article Data Science: An Action Plan for Expanding the Technical Areas of the Field of Statistics.
- 2002- April- The ICSU (International Council for Science): Committee on Data for Science and Technology (CODATA) starts Data Science Journal- this publication is to focus on issues pertaining to data systems- description, publication, application, and also legal issues.
- 2003- January- Columbia University publishes journal The Journal of Data Science- a platform that allows data workers to exchange ideas.
- 2005- National Science Board publishes Long-lived Digital Data Collections: Enabling Research and Education in the 21st Century- this provides a new definition to the term “data scientists”.
- 2007- Jim Gray, Turing awardee, envisions data-driven science as the fourth paradigm of science.
- 2012- Harvard Business Review article attributes coinage of the term to DJ Patil and Jeff Hammerbacher in 2008.
- 2013- IEEE launches a task force on Data Science and Advanced Analytics; first European Conference on Data Analysis (ECDA)organized in Luxembourg, European Association for Data Science (EuADS) comes into existence.
- 2014- IEEE launches first international conference International Conference on Data Science and Advanced Analytics; General Assembly launches student-paid Bootcamp, The Data Incubator launches data science fellowship for free.
- 2015- Springer launches International Journal on Data Science and Analytics.
# Data science tools:
-  Machine Learning for Pattern Discovery
-  Machine Learning for Making Predictions
- Predictive Causal Analytics
- Prescriptive Analytics
# MARKDOWN SYNTAX
Adding italics and bold:
> '*Italics* **Bold**'
# Adding headers (titles) of various sizes:
# header one ## header two
# Adding hyperlinks and images:
'[Link](http://a.com)'
# Adding block quotes:
'> Blockquote'
# Adding lists:
'* * *'
 # Adding horizontal lines:
'‐‐‐'
# Adding inline code:
`Inline code with backticks`
# Adding code blocks
``` code ```
# JUPYTER NOTEBOOK SPECIAL COMMAND
# Displaying the code execution history:
- %history -p

# Types of modes in Jupyter:
- Jupyter is in edit mode whenever we type in a cell — a small pencil icon appears to the right of the menu bar.
- Jupyter is in command mode whenever we press Esc or whenever we click outside of the cell — the pencil to the right of the menu bar disappears.
- State refers to what a computer remembers about a program.
- We can convert a code cell to a Markdown cell to add text to explain our code. Markdown syntax allows us to use keyboard symbols to format our text.

# Some of the most useful keyboard shortcuts we can use in command mode are:
- Ctrl + Enter: run selected cell
- Shift + Enter: run cell, select below
- Alt + Enter: run cell, insert below
- Up: select cell above
- Down: select cell below
- Enter: enter edit mode
- A: insert cell above
- B: insert cell below
- D, D (press D twice): delete selected cell
- Z: undo cell deletion
- S: save and checkpoint
- Y: convert to code cell
- M: convert to Markdown cell
# Some of the most useful keyboard shortcuts we can use in edit mode are:
- Ctrl + Enter: run selected cell
- Shift + Enter: run cell, select below
- Alt + Enter: run cell, insert below
- Up: move cursor up
- Down: move cursor down
- Esc: enter command mode
- Ctrl + A: select all
- Ctrl + Z: undo
- Ctrl + Y: redo
- Ctrl + S: save and checkpoint
- Tab : indent or code completion
- Shift + Tab: tooltip


# Day 2(21-07-2020):
Completed my first assignment course on kaggle <b>"Python for data science"</b>.
[check here the assignments](https://github.com/pavi-ninjaac/Data_Science_internship_program_Technocolaps_July2020/tree/master/Assignment/python_for_data_science_kaggle_handsOn)

# Day3 (22-07-2020):
completed the sencond assignment course on kaggle <b>"Python Data manupulation Pandas"</b>
[check here the assignments](https://github.com/pavi-ninjaac/Data_Science_internship_program_Technocolaps_July2020/tree/master/Assignment/Python_Data_manupulation_Pandas_kaggleHandson)

# Day 4 (23-07-2020):
completed my 3rd assignment course on kaggle <b> Data visualization with seaborn</b>
[check here the assignments](https://github.com/pavi-ninjaac/Data_Science_internship_program_Technocolaps_July2020/tree/master/Assignment/Data_Visualization_seaborn_kaggle_handson)


# leasson summary:
### Trends - A trend is defined as a pattern of change.
- sns.lineplot - Line charts are best to show trends over a period of time, and multiple lines can be used to show trends in more than one group.
- Relationship - There are many different chart types that you can use to understand relationships between variables in your data.
- sns.barplot - Bar charts are useful for comparing quantities corresponding to different groups.
- sns.heatmap - Heatmaps can be used to find color-coded patterns in tables of numbers.
- sns.scatterplot - Scatter plots show the relationship between two continuous variables; if color-coded, we can also show the relationship with a third categorical variable.
- sns.regplot - Including a regression line in the scatter plot makes it easier to see any linear relationship between two variables.
- sns.lmplot - This command is useful for drawing multiple regression lines, if the scatter plot contains multiple, color-coded groups.
- sns.swarmplot - Categorical scatter plots show the relationship between a continuous variable and a categorical variable.
### Distribution - We visualize distributions to show the possible values that we can expect to see in a variable, along with how likely they are.
- sns.distplot - Histograms show the distribution of a single numerical variable.
- sns.kdeplot - KDE plots (or 2D KDE plots) show an estimated, smooth distribution of a single numerical variable (or two numerical variables).
- sns.jointplot - This command is useful for simultaneously displaying a 2D KDE plot with the corresponding KDE plots for each individual variable.
### Changing styles with seaborn
All of the commands have provided a nice, default style to each of the plots. However, you may find it useful to customize how your plots look, and thankfully, this can be accomplished by just adding one more line of code!

As always, we need to begin by setting up the coding environment. (This code is hidden, but you can un-hide it by clicking on the "Code" button immediately below this text, on the right.)

We'll work with the same code that we used to create a line chart in a previous tutorial. The code below loads the dataset and creates the chart.

# Day 5 (24-07-2020):
completed my 4th assignment course on kaggle <b> INtro to SQL and bigqueries</b>
[check here the assignments](https://github.com/pavi-ninjaac/Data_Science_internship_program_Technocolaps_July2020/tree/master/Assignment/IntroTo_sql_bigqueries)

# Day 6 (25-07-2020):
Completed my first Mini project using the handwashing dataset.
[check here the mini project](https://github.com/pavi-ninjaac/Data_Science_internship_program_Technocolaps_July2020/tree/master/MiniProject_1)

# Day 7-9(26-07-2020 -- 28-07-2020)
Reviweced and Elvaluated my Assignments and mini project 1

# Day 10(29-07-2020)
MiniProject 2- started and completed task1 and task 2
[Check here the work for Task-1](https://github.com/pavi-ninjaac/Data_Science_internship_program_Technocolaps_July2020/tree/master/MiniProject2/task1/Data_Exploration_and_Cleaning)<br/>
[Check here the work for Task-2](https://github.com/pavi-ninjaac/Data_Science_internship_program_Technocolaps_July2020/tree/master/MiniProject2/task2/Exploring_Remaining_Financial_Features_in_the_Dataset)<br/>

# Day 11(30-07-2020)
MiniProject 2- completed task3, task4
[Check here the work for task-3](https://github.com/pavi-ninjaac/Data_Science_internship_program_Technocolaps_July2020/tree/master/MiniProject2/task3/Performing_Logistic_Regression)<br/>
[Check here the work for task-4](https://github.com/pavi-ninjaac/Data_Science_internship_program_Technocolaps_July2020/tree/master/MiniProject2/task4/Fitting_a_Logistic_Regression_Model)<br/>
Learned deeply abut the ROC and PR curves (precision-recall)

# Day 12(31-07-2020)
MiniProject 2- completed task5
[Check here the work for task 5](https://github.com/pavi-ninjaac/Data_Science_internship_program_Technocolaps_July2020/tree/master/MiniProject2/task5/Cross-Validation_and_Feature_Engineering)<br/>
Learned about the 

# Day 13(01-08-2020)
MiniProject 2- completed task6
[Check here the work for task 6](https://github.com/pavi-ninjaac/Data_Science_internship_program_Technocolaps_July2020/tree/master/MiniProject2/task6/Cross-Validation_Grid_Search_with_Random_Forest)

# Day 14 (02-082020)
MiniProject 2- learning things for  task7
[Check here the work for task 7]()

# Day 15 (03-08-2020)
did task7

# Day 16(04-08-2020)

# Day 17-24(05-08-2020 - 12-08-2020)
preparing my self for the final project 
the link for gitbok is https://technocollabs.gitbook.io/final-project-in-data-science/
