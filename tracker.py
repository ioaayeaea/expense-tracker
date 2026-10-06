# Project: Expense Tracker
# Installment: 3
# Author: Fiona Caye Calleja 
# Tracker does math

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

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * tax_percent / 100
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)
print("Made by: Fiona Caye Calleja | Installment 3")

   