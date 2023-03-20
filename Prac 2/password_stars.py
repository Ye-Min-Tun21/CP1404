def main():
    minimum_password_length = 8
    password = get_password(minimum_password_length)
    print_asterisks(password)

def get_password(minimum_password_length):
    while True:
        password = input("Enter a password: ")
        if len(password) < minimum_password_length:
            print("Password is too short. Please try again.")
        else:
            return password

def print_asterisks(password):
    print("*" * len(password))

if __name__ == '__main__':
    main()
