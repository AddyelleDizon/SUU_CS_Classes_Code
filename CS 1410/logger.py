# This will be the Singleton class file.

# The first step is to create the Singleton class.
# In this instance, I have chosen to create the "Logger" class.
class Logger:

    # The next step is to create the _instance. Initially set to "None". This is to show that the instance of the class
    # has not been created yet.
    _instance = None

    # We then define the constructor.
    def __init__(self):

        # This "if" statement is used for raising any errors. 
        if Logger._instance is not None:

            # In this instance, we would raise an Exception if the _instance is not None.
            raise Exception("This is a singleton class, use get_instance() to get the instance.")
        
        else:

            # Otherwise, we would initialize the instance, then add it to a list.
            self.logs = []
            print("Logger instance created.")

    # We would then create the static method.
    @staticmethod
    def get_instance():

        # This "if" statement is to apply the creation of one class.
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    # This log() method is just a method to add a "log" entry.
    def log(self, message):
        self.logs.append(message)

        # Self Note: Finally learned how to use the f"{statement}" 
        print(f"Log added: {message}")

    # This method is to return the "logs" recorded.
    def get_logs(self):
        return self.logs