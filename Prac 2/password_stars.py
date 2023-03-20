minimum_password_length = 8

while True:
    password = input("Enter a password: ")
    if len(password) < minimum_password_length:
        print("Password is too short. Please try again.")
    else:
        print("*" * len(password))
        break