"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

TARGET_SALES = 1000

sales = float(input("Enter sales: $"))
if sales < TARGET_SALES:
    print("Bonus 10%")
    bonus = sales * 0.1


else:
    print("Bonus 20%")
    bonus = sales * 0.1
print(f"Bonus is ${bonus}")

#Version 2 with loop

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= TARGET_SALES:
        bonus = sales * 0.2

    else:
        bonus = sales * 0.1

    print(f"Bonus is ${bonus}")
    sales = float(input("Enter sales: $"))