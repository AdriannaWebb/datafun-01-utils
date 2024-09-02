''' ITERATION 4

Module: Webb Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. .
A good byline could be used in every Python analytics project we do.

Process:
I'll test it in an online interpreter to ensure this version runs correctly before continuing.
Process:
In this fourth iteration, I introduce some basic statistics using Python:
    - min()
    - max()
    - The statistics module offers methods to calculate mean and standard deviation
'''
######################################
# Import Modules at the Top
######################################

import statistics

#######################################
# Declare global variables - keep byline at the end
# We will use this information in a smarter byline
#######################################

# Boolean variable to indicate if the client has a black cat
has_black_cat: bool = True

# Integer variable for the number of black cats a client has
number_of_black_cats: int = 1

# List of strings representing the skills of each black cat
skills_offered: list = ["Mouse Catching", "Machine Learning", "Making A Mess"]

# List of floats representing individual cat satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#######################################
# Calculate Basic Statistics
#   Do this BEFORE we declare the byline
#   So the values have been calculated
#   and are ready for use in the byline.
#######################################

# Calculate basic stats using built-in functions min(), max() and statistics module functions mean() and stdev().
min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)

#######################################
# Declare a global variable named byline.
# Make it a multiline f-string to show our information.
#######################################

byline: str = f"""
-------------------------------------------------
Webb Analytics: Analytics for the Web, by Webb
-------------------------------------------------
Has Black Cat: {has_black_cat}
Number of Black Cats:        {number_of_black_cats}
Skills Offered:            {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(byline)

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()

