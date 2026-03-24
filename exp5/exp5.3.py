# Initial inventory
"""
Created on Tue Mar 24 10:35:19 2026

@author: sujit
"""
# Initial inventory
inventory = {
    "Rice": 50,
    "Sugar": 30,
    "Oil": 20
}


item = input("Enter item name: ")
quantity = int(input("Enter quantity to add: "))

if item in inventory:
    inventory[item] += quantity
else:
    inventory[item] = quantity

print("\nUpdated Inventory:")
for key, value in inventory.items():
    print(key, ":", value)
