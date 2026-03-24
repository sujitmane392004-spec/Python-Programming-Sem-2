# find the sum and average of elemant
"""
Created on Tue Mar 24 10:15:49 2026

@author: SUJIT
"""

n = int(input("Enter number of elements: ")) 
numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: ")) 
    numbers.append(num)
 
total = sum(numbers)
average = total / n if n > 0 else 0
print("List:", numbers) 
print("Sum of elements:", total)
print("Average of elements:", average)
