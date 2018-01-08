# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import sys
import os
import csv

def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    parsed_data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            parsed_data.append(list(map(str.strip, row)))
    return parsed_data

def get_index_with_min_abs_score_difference(parsed_data):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    # Get the index for 'for' and 'against' columns:
    i_for = parsed_data[0].index('Goals')
    i_against = parsed_data[0].index('Goals Allowed')
    
    # Iterate through the list and remember the index which improves 
    # the abs difference:
    min_abs_diff = None
    for i in range(2, len(parsed_data)):
        abs_diff = abs(int(parsed_data[i][i_for]) - int(parsed_data[i][i_against]))
        if min_abs_diff is None or abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
            min_index = i
            
    # Return the index:
    return min_index
    
    
def get_team(index_value, parsed_data):
    """Returns the team name at a given index.
    
    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
    Returns: the team name
    """
    # Find the index for the team name:
    i_team = parsed_data[0].index('Team')
    return parsed_data[index_value][i_team]

footballTable = read_data('football.csv')
minRow = get_index_with_min_abs_score_difference(footballTable)
print(str(get_team(minRow, footballTable)))

