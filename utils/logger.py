from datetime import datetime


def log_execution(option):
    with open("outputs/execution_log.txt", "a") as file:
        now = datetime.now()
        file.write(
            f"Date: {now.strftime('%Y-%m-%d')} | "
            f"Time: {now.strftime('%H:%M:%S')} | "
            f"Menu Option: {option}\n"
        )
