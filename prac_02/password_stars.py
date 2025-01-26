max_length = 15
min_length = 3


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input("What is the password?: ")
    while len(password) > max_length or len(password) < min_length:
        print("Password cannot be less than 3 and greater than 15")
        password = input("What is the password?: ")
    return password


def print_asterisks(password):
    print("*" * len(password))


main()

