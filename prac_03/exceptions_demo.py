"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?
# ValueError will occur when we input anything except int (number) since there is an int function in the code.

# When will a ZeroDivisionError occur?
# ZeroDivisionError will occur when we specify the denominator as 0.

# Could you change the code to avoid possibility a ZeroDivisonError?
# Yes, we can change the code to avoid possibilty of a ZeroDivisionError.

