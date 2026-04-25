# using the date time module to print the current date, time, and weekday
"""
Created on Mon Apr 20 14:42:41 2026

@author: sujit
"""

import datetime

# Get current date and time
now = datetime.datetime.now()

# Print current date
print("Current Date:", now.strftime("%Y-%m-%d"))

# Print current time
print("Current Time:", now.strftime("%H:%M:%S"))

# Print current weekday
print("Weekday:", now.strftime("%A"))
