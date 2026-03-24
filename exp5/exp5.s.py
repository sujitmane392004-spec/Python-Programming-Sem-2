#  Creating an empty dictionary
"""
Created on Tue Mar 24 10:15:00 2026

@author: sujit
"""

student = {}

#Adding Key-value pairs
student["name"]= "Varad"
student["age"] = 18
student["course"] = "python"

print("Dictionary after adding elements:")
print(student)

#Updating a value
student["age"] = 19

print("\nDictionary after updating a value:")
print(student)

# Deleting a key-value pair
del student["course"]

print("\nDictionary after deleting a key-value pair:")
print(student)
