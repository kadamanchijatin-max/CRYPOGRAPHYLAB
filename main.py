from utils.logger import log_execution
from analysis.text_analyzer import analyze_file


def menu():
    while True:
        print("\n===== CryptoLabX =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Attack")
        print("4. Analyze Text File")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            log_execution("Encrypt")
            print("Encrypt - Coming Soon")

        elif choice == "2":
            log_execution("Decrypt")
            print("Decrypt - Coming Soon")

        elif choice == "3":
            log_execution("Attack")
            print("Attack - Coming Soon")

        elif choice == "4":
            log_execution("Analyze Text")

            print("\nAvailable datasets:")
            print("1. sample1.txt")
            print("2. sample2.txt")
            print("3. sample3.txt")
            print("4. sample4.txt")
            print("5. sample5.txt")

            file_choice = input("Choose file: ")

            files = {
                "1": "datasets/sample1.txt",
                "2": "datasets/sample2.txt",
                "3": "datasets/sample3.txt",
                "4": "datasets/sample4.txt",
                "5": "datasets/sample5.txt"
            }

            if file_choice in files:
                analyze_file(files[file_choice])
            else:
                print("Invalid dataset choice")

        elif choice == "5":
            log_execution("Exit")
            print("Exiting CryptoLabX...")
            break

        else:
            log_execution("Invalid Choice")
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
