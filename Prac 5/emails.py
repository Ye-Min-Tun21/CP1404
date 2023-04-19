def extract_name(email):
    username, domain = email.split("@")
    names = username.split(".")
    full_name = " ".join(name.title() for name in names)
    response = input(f"Is your name {full_name}? (Y/n) ").lower()
    if response == "" or response == "y":
        return full_name
    else:
        name = input("Name: ")
        return name


def store_users():
    users = {}

    while True:
        email = input("Email: ")
        if email == "":
            break
        name = extract_name(email)
        users[email] = name

    for email, name in users.items():
        print(f"{name} ({email})")


store_users()
