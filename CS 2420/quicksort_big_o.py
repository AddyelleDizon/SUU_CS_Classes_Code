import random
import time


def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)


def quick_sort_helper(a_list, first, last):
    if first < last:
        split = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split - 1)
        quick_sort_helper(a_list, split + 1, last)


def partition(a_list, first, last):
    pivot_val = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            left_mark = left_mark + 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = (
                a_list[right_mark],
                a_list[left_mark],
            )
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    return right_mark

def random_list(amnt):
    random_numbers = [random.randint(1, amnt) for i in range(amnt)]
    random.shuffle(random_numbers)
    return random_numbers

def measure_quicksort(amnt):
    rand = random_list(amnt)

    start = time.time()
    quick_sort(rand)
    end = time.time()
    
    elapsed = end - start
    print(f"Time elapsed for {amnt:.0f} items (quicksort):      {elapsed:.5f} seconds")

amounts = [1000, 10000, 100000, 1000000]
for i in amounts:
    measure_quicksort(i)
    print("\n")

