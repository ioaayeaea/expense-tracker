# Project: Expense Tracker
# Installment: 2
# Author: Fiona Caye Calleja 
# Personal expense tracker landing page

print("=" * 40)
print("            EXPENSE TRACKER")
print("       Know where your money goes.")
print("=" * 40)

print("MAIN MENU")
print("    [1] Add an expense")
print("    [2] View all expenses")
print("    [3] Show total spent")
print("    [4] Exit")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)
print("Made by: Fiona Caye Calleja |  Installment 2")
