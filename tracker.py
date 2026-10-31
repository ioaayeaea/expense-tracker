# Project: Expense Tracker
# Installment: 5
# Author: Fiona Caye Calleja
# The Menu Comes Alive

print("=" * 40)
print("            EXPENSE TRACKER")
print("       Know where your money goes.")
print("          INSTALLMENT 5")
print("=" * 40)

name = input("What's your name? ")
tax_rate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

tax_percent = tax_rate / 100
subtotal = 0.0
count = 0

print(f"Welcome, {name}!")

menu = """
========== MAIN MENU ==========
[1] Add an expense
[2] View all expenses (coming soon)
[3] Show total spent
[4] Exit
===============================
"""

choice = 0

while choice != 4:
    print(menu)

    try:
        choice = int(input("Choose 1-4: "))
    except ValueError:
        print("Please choose 1, 2, 3, or 4.")
        continue

    if choice == 1:
        try:
            amount = float(input("Amount? "))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            subtotal += amount
            count += 1

            if amount > 200:
                print("Huge expense - are you sure?")
            elif amount > 100:
                print("Big expense.")
            elif amount > 50:
                print("Moderate expense.")
            else:
                print("Small expense.")

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == 2:
        print(
            "Coming soon: the tracker can't remember "
            "each item yet."
        )

    elif choice == 3:
        tax = subtotal * tax_percent
        grand_total = subtotal + tax
        left = budget - grand_total

        print("-" * 40)
        print("SUMMARY")
        print(f"{'Expense count:':<24}{count:>12}")
        print(f"{'Subtotal:':<24}${subtotal:>11.2f}")
        print(f"{'Tax:':<24}${tax:>11.2f}")
        print(f"{'Grand total:':<24}${grand_total:>11.2f}")

        if grand_total > budget:
            print(f"Over budget by ${grand_total - budget:.2f}!")
        elif grand_total > budget * 0.90:
            print(f"Careful: only ${left:.2f} left.")
        else:
            print(f"Within budget. ${left:.2f} left.")

        print("-" * 40)

    elif choice == 4:
        print(f"Goodbye, {name}!")

    else:
        print("Please choose 1, 2, 3, or 4.")

print("Made by: Fiona Caye Calleja | Installment 5")