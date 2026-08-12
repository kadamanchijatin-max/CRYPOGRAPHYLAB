def login():
    print("\n===== DRONE MANAGEMENT SYSTEM LOGIN =====")

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "drone123":
        print("\nLogin successful!")
        return True

    if username == "operator" and password == "operator123":
        print("\nLogin successful!")
        return True

    print("\nInvalid username or password.")
    return False