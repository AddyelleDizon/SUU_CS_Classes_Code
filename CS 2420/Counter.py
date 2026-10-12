class Counter:
    def __init__(self):
        self._count = 0

    def incrementCount(self):
        self._count += 1

    def resetCount(self):
        self._count = 0

    def print_count(self):
        print("Current count: %d" % (self._count))

    def input_count(self):
        user_input = int(input("Enter a new count: "))
        self._count = user_input
        if self._count == ValueError:
            print("Invalid input. Please enter an integer.")

    def get_count(self):
        return self._count

    def set_count(self, value):
        if isinstance(value, int):
            self._count = value
        else:
            raise ValueError("Count must be an integer.")

