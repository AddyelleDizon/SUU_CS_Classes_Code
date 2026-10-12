import random
import time

def sequential_search(a_list, item):
    pos = 0

    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        pos = pos + 1

    return False

def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return False

def fill_list(amnt):
    size = [i for i in range(amnt)]
    return size

def fill_dict(amnt):
    size = {f"Key_{i}": i*2 for i in range(amnt)}
    return size

def randomize(amnt):
    size = [i for i in range(amnt)]
    hundrand = random.sample(size, 100)
    return hundrand

def search_bin(amnt):
    items = fill_list(amnt)
    rand = randomize(amnt)

    start = time.time()
    for r in rand:
        binary_search(items, r)
        end = time.time()
    
    elapsed = end - start
    print(f"Time elapsed for {amnt:.0f} items (binary): {elapsed:.5f} seconds")

def search_seq(amnt):
    items = fill_list(amnt)
    rand = randomize(amnt)

    start = time.time()
    for r in rand:
        sequential_search(items, r)
        end = time.time()
    
    elapsed = end - start
    print(f"Time elapsed for {amnt:.0f} items (sequential): {elapsed:.5f} seconds")
        
def search_standard_dict(amnt):
    keys = fill_dict(amnt)
    rand = randomize(amnt)

    start = time.time()
    for k in rand:
        k in keys
    end = time.time()
    
    elapsed = end - start
    print(f"Time elapsed for {amnt:.0f} items (standard dictionary): {elapsed:.5f} seconds")

amounts = [1000, 10000, 100000, 1000000]
for i in amounts:
    search_standard_dict(i)
    search_bin(i)
    search_seq(i)
    print("\n")