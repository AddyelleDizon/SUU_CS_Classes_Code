import random
import time

def bubble_sort(a_list):
    for i in range(len(a_list)):
        for j in range(len(a_list)-i-1):
            if a_list[j] > a_list[j + 1]:
                (a_list[j], a_list[j + 1]) = (a_list[j + 1], a_list[j])

def bubble_sort_short(a_list):
    for i in range(len(a_list)):
        exchanges = False
        for j in range(len(a_list)-i-1):
            if a_list[j] > a_list[j + 1]:
                exchanges = True
                (a_list[j], a_list[j + 1]) = (a_list[j + 1], a_list[j])
        if not exchanges:
            break

def selection_sort(a_list):
    for i, item in enumerate(a_list):
        min_idx = len(a_list) - 1
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_idx]:
                min_idx = j
        if min_idx != i:
            a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]


def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i

        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos = cur_pos - 1
        a_list[cur_pos] = cur_val

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for pos_start in range(sublist_count):
            gap_insertion_sort(a_list, pos_start, sublist_count)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        cur_val = a_list[i]
        cur_pos = i
        while cur_pos >= gap and a_list[cur_pos - gap] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - gap]
            cur_pos = cur_pos - gap
        a_list[cur_pos] = cur_val

def merge_sort(a_list):
    #print("Splitting", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    #print("Merging", a_list)

def random_list(amnt):
    random_numbers = [random.randint(1, amnt) for i in range(amnt)]
    random.shuffle(random_numbers)
    return random_numbers

def measure_bubble(amnt):
    rand = random_list(amnt)

    start = time.time()
    bubble_sort(rand)
    end = time.time()
    
    elapsed = end - start
    print(f"Time elapsed for {amnt:.0f} items (bubble):     {elapsed:.5f} seconds")

def measure_selection(amnt):
    rand = random_list(amnt)

    start = time.time()
    selection_sort(rand)
    end = time.time()
    
    elapsed = end - start
    print(f"Time elapsed for {amnt:.0f} items (selection):  {elapsed:.5f} seconds")

def measure_insertion(amnt):
    rand = random_list(amnt)
    
    start = time.time()
    insertion_sort(rand)
    end = time.time()
    
    elapsed = end - start
    print(f"Time elapsed for {amnt:.0f} items (insertion):  {elapsed:.5f} seconds")

def measure_shell(amnt):
    rand = random_list(amnt)

    start = time.time()
    shell_sort(rand)
    end = time.time()
    
    elapsed = end - start
    print(f"Time elapsed for {amnt:.0f} items (shell):      {elapsed:.5f} seconds")

def measure_merge(amnt):
    rand = random_list(amnt)

    start = time.time()
    merge_sort(rand)
    end = time.time()
    
    elapsed = end - start
    print(f"Time elapsed for {amnt:.0f} items (merge):      {elapsed:.5f} seconds")

amounts = [1000, 10000, 100000, 1000000]
for i in amounts:
    measure_merge(i)
    measure_shell(i)
    measure_insertion(i)
    measure_selection(i)
    measure_bubble(i)
    print("\n")


