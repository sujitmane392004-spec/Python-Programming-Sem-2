# check leap year
"""
Created on Tue Feb 10 09:54:27 2026

@author: sujit mane
"""
year = int(input("Enter year:"))
if (year % 400 == 0) or (year%4==0 and year % 100!= 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
