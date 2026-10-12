from binary_search_tree import BinarySearchTree
from avl_tree import AVLTree
import tail_recursion
import random 
import time
 
def measure_search(search, amnt):
    bst = BinarySearchTree()

    bst_start_time = time.time()
    for i in search:
        bst_time = bst.get(i)
    bst_end_time = time.time()

    bst_total_time = bst_end_time - bst_start_time

    avl = AVLTree()
    avl_start_time = time.time()
    for i in search:
        avl_time = avl.get(i)
    avl_end_time = time.time()

    avl_total_time = avl_end_time - avl_start_time

    print(f"Time elapsed for {amnt:.0f} items (search_bst):      {bst_total_time:.5f} seconds")
    print(f"Time elapsed for {amnt:.0f} items (search_avl):      {avl_total_time:.5f} seconds")

def measure_insert(data, amnt):
    bst = BinarySearchTree()

    bst_start_time = time.time()
    for i in data:
        bst_time = bst.put(i, i)
    bst_end_time = time.time()

    bst_total_time = bst_end_time - bst_start_time

    avl = AVLTree()
    avl_start_time = time.time()
    for i in data:
        avl_time = avl.put(i, i)
    avl_end_time = time.time()

    avl_total_time = avl_end_time - avl_start_time

    print(f"Time elapsed for {amnt:.0f} items (insert_bst):      {bst_total_time:.5f} seconds")
    print(f"Time elapsed for {amnt:.0f} items (insert_avl):      {avl_total_time:.5f} seconds")

def random_list(amnt):
    random_numbers = [random.randint(1, amnt) for i in range(amnt)]
    random.shuffle(random_numbers)
    return random_numbers

def fill_list(amnt):
    size = [i for i in range(amnt)]
    return size

amounts = [1000, 10000, 100000, 1000000]
for a in amounts:
    rand = random_list(a)
    sort = fill_list(a)
    print("Random order")
    measure_insert(rand, a)
    measure_search(rand, a)
    print("Sorted order")
    measure_insert(sort, a)
    measure_search(sort, a)
