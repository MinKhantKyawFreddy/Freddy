FILENAME = "name.txt"
# Write the name to  name.txt
name = input("Enter your name: ")
with open(FILENAME, "w") as file:
    file.write(name)

with open(FILENAME, "r") as file:
    name_from_file = file.read().strip()
print(f"Hi {name_from_file}!")

with open("numbers.txt", "r") as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())
print(first_number + second_number)

total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print(total)
