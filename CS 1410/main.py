# Importing the other code into __main__.
from logger import Logger

def main():
    # Creation of multiple instances of the Logger class.
    logger1 = Logger.get_instance()
    logger2 = Logger.get_instance()

    # Ensurance that both logger1 and logger2 refer to the same class "Logger".
    if logger1 is logger2:
        print("Both logger1 and logger2 refer to the same instance.")

    # Logging some basic messages.
    logger1.log("This is my first log message. Signed, Addyelle.")
    logger1.log("This is my second log message. Signed, Addyelle.")

    # This retrieves logs through logger2 (which is the same instance)
    print("Logs from logger2:")
    for log in logger2.get_logs():
        print(log)

if __name__ == "__main__":
    main()






    