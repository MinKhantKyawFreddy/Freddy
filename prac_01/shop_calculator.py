DISCOUNT_PRICE = 100
DISCOUNT = 0.1
number_of_items = int(input("Number of items: "))
total = 0
while number_of_items <= 0:
    print("Invalid number of items!")

else:
    for i in range(number_of_items):
        price = float(input("Price of item: "))
        total += price
    if total > DISCOUNT_PRICE:
        total = total - (total * DISCOUNT)
print(f"Total price for {number_of_items} items is ${total:.2f}")



