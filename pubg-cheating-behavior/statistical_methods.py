import numpy as np
from data_processing import *
from team_analysis import *

def round_by_magnitude(value):
    """
    Rounds the value based on its magnitude:
    - Thousands or higher: 0 or 1 decimal place.
    - Ones or tens: 2 or 3 decimal places.
    """
    if abs(value) >= 1000:
        return round(value, 1)
    elif abs(value) >= 10:
        return round(value, 2)
    else:
        return round(value, 3)


def calculate_mean_and_confidence_intervals(aggregate_cheater_counts, output_format = "summary"):
    """
    Calculate the expected counts (mean) and 95% confidence intervals for the number of cheaters in each team.

    arguments:
    aggregate_cheater_counts (list of tuples): Each tuple contains the number of cheaters in each team for a single shuffle.

    returns:
    expected_counts (list): The expected counts (mean) for each number of cheaters in teams.
    con_interval (list of tuples): The 95% confidence intervals for each number of cheaters in teams.
    """

    # Check if the first element of aggregate_cheater_counts is a single number (int or float). If so, wrap it in a list for consistent processing.
    if isinstance(aggregate_cheater_counts[0], (int, float)):  
        aggregate_cheater_counts = [aggregate_cheater_counts]

    means = []  # List to store mean counts (expected counts)
    con_interval = []  # List to store confidence intervals

    if output_format == "detailed":
        print("Randomised counts:")
    elif output_format == "summary":
        print("Randomized counts for starting cheating:")

    for index, counts in enumerate(aggregate_cheater_counts):
        mean = np.mean(counts)  # Calculate mean (expected count)
        std_dev = np.std(counts, ddof=1)  # calculate standard deviation
        n = len(counts)  # Number of shuffles
        ci_margin = 1.96 * (std_dev / np.sqrt(n))  # Confidence interval margin
        ci_lower, ci_upper = mean - ci_margin, mean + ci_margin

        # Apply rounding rules
        mean_rounded = round_by_magnitude(mean)
        ci_lower_rounded = round_by_magnitude(ci_lower)
        ci_upper_rounded = round_by_magnitude(ci_upper)

        means.append(mean_rounded)
        con_interval.append((ci_lower_rounded, ci_upper_rounded))

         # Print output based on the specified format
        if output_format == "detailed":
            print(f"Teams with {index} cheaters: Mean = {mean_rounded}, "
                  f"95% CI = ({ci_lower_rounded}, {ci_upper_rounded})")
        elif output_format == "summary" and index == 0:  # For summary, only show the first count
            print(f"Expected Count (Mean) = {mean_rounded}, "
                  f"95% CI = ({ci_lower_rounded}, {ci_upper_rounded})")

    return means, con_interval


