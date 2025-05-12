"""
File: utils_bless.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects.
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Blessing Aganaga
"""

#####################################
# Import Modules
#####################################

import statistics


#####################################
# Declare Global Variables
#####################################

# Business-specific info
has_international_clients: bool = True
years_in_operation: int = 3
average_client_satisfaction: float = 4.8
skills_offered: list = ["Data Engineering", "BI Dashboards", "Data Storytelling"]

# Client feedback scores for satisfaction
client_satisfaction_scores: list = [4.9, 4.7, 4.8, 5.0, 4.6]

# Statistics
min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)

# Byline output
byline: str = f"""
---------------------------------------------------------
Blessing Analytics: Empowering Smarter Business Decisions
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score:    {mean_score:.2f}
Standard Deviation:         {stdev_score:.2f}
"""

#####################################
# Define global functions
#####################################

def get_byline() -> str:
    """Return the company byline."""
    return byline


#####################################
# Define main function
#####################################

def main() -> None:
    """Print the byline when this file is run as a script."""
    print("START main() in utils_steph.py")
    print(get_byline())
    print("END main() in utils_steph.py")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
