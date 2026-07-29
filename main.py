from datetime import datetime


def write_log(option):
    with open("log.txt", "a") as file:
        now = datetime.now()
        file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {option}\n")


def menu():
    while True:
        print("\n===== CryptoLabX =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Attack")
        print("4. Analyze")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            write_log("Encrypt")
            print("Encrypt - Coming Soon")

        elif choice == "2":
            write_log("Decrypt")
            print("Decrypt - Coming Soon")

        elif choice == "3":
            write_log("Attack")
            print("Attack - Coming Soon")

        elif choice == "4":
            write_log("Analyze")
            print("Analyze - Coming Soon")

        elif choice == "5":
            write_log("Exit")
            print("Exiting CryptoLabX...")
            break

        else:
            write_log("Invalid Choice")
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
