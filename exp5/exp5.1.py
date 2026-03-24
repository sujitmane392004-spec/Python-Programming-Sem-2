#  Create dictionary
"""
Created on Tue Mar 24 10:29:15 2026

@author: User
"""

library = {
    "Maths": 250,
    "Physics": 300,
    "Chemistry": 280
}


print("Original Library Data:")
print(library)


book = input("Enter book name to update: ")


if book in library:
    new_price = float(input("Enter new price: "))
    library[book] = new_price
    print("Price updated successfully!")
else:
    print("Book not found!")


print("Updated Library Data:")
print(library)
