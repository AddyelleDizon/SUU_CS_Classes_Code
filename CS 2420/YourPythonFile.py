import random
import time

sizes = [1000, 100000, 1000000]

def List_Test():                                            # Notes are for future reference; I tend to forget why I wrote it a specific way
    for size in sizes:
        my_list = list(range(size))                         # List creation

        random_indices = random.sample(range(size), 1000)   # Find a sample of a random index from the range(size) to 1000
        start_time = time.time()                            # Self explanatory
        
        for index in random_indices:                        # For any index in the sample, replace with a random integer
            my_list[index] = random.randint
        set_time = time.time() - start_time

        start_time = time.time()                            # Same as setting, for any index in the sample, get a random integer
        
        for index in random_indices:
            get_location = my_list[index]
        get_time = time.time() - start_time

        print(f"A list with size = {size}: Start time = {set_time:.6f}s, Time Taken = {get_time:.6f}s")

# Essentially the same thing when testing for lists, just with dictionaries
def Dict_Test():
    for size in sizes:
        my_dict = {i: i for i in range(size)}

        random_indices = random.sample(range(size), 1000)
        start_time = time.time()
        
        for index in random_indices:
            my_dict[index] = random.randint
        set_time = time.time() - start_time

        start_time = time.time()
        
        for index in random_indices:
            get_location = my_dict[index]
        get_time = time.time() - start_time

        print(f"A dictionary with size = {size}: Start time = {set_time:.6f}s, Time Taken = {get_time:.6f}s")

def Delete_Test():
    for size in sizes:
        my_list = list(range(size))                         # Creation of list
        random_indices = random.sample(range(size), 1000)
        start_time = time.time()

        for index in sorted(random_indices, reverse=True):  # There was an issue in index shifting (out of bounds), so doing it in reverse to avoid that
            del my_list[index]                              # Deleting indices in the list
        list_del_time = time.time() - start_time

        my_dict = {i: i for i in range(size)}               # Creation of dictionary
        random_indices = random.sample(range(size), 1000)
        start_time = time.time()

        for index in random_indices:
            del my_dict[index]                              # Same as list, deleting random indices in a dictionary
        dict_del_time = time.time() - start_time

        print(f"A list with size = {size}: Delete time = {list_del_time:.6f}s")
        print(f"A dictionary with size = {size}: Delete time = {dict_del_time:.6f}s")

def main():
    print("Task 1: List Tests")
    List_Test()

    print("\nTask 2: Dictionary Tests")
    Dict_Test()

    print("\nTask 3: Deletion Tests")
    Delete_Test()

main()
