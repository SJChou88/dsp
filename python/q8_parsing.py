# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

with open('/Users/stephenchou/ds/metis/metisgh/prework/dsp/python/football.csv') as f:
    reader = csv.DictReader(f)
    smallestgd = None
    for row in reader:
        absgd = abs(int(row['Goals'])-int(row['Goals Allowed']))
        if smallestgd == None:
            smallestgd = absgd
            smallestname = row['Team']
        elif smallestgd > absgd:
            smallestgd = absgd
            smallestname = row['Team']
    print(smallestname)