# Find factorial number
"""
Created on Tue Feb 10 10:14:46 2026

@author: sujit mane
"""

n = int(input("Enter number:"))
fact = 1
for i in range(1,n + 1):
    fact = fact * i
print("Factorial:",fact)
