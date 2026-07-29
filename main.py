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
            print("Encrypt - Coming Soon")

        elif choice == "2":
            print("Decrypt - Coming Soon")

        elif choice == "3":
            print("Attack - Coming Soon")

        elif choice == "4":
            print("Analyze - Coming Soon")

        elif choice == "5":
            print("Exiting CryptoLabX...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
