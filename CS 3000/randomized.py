import random
import time

def randomized_partition(A, p, r):
    pivot_index = random.randint(p, r)
    A[pivot_index], A[r] = A[r], A[pivot_index]

    pivot = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def randomized_select(A, p, r, i):
    if p == r:
        return A[p]

    q = randomized_partition(A, p, r)
    k = q - p + 1

    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)


def timed_randomized_select(A, i):
    start = time.perf_counter()
    result = randomized_select(A, 0, len(A) - 1, i)
    end = time.perf_counter()

    elapsed = end - start
    return result, elapsed

A = [random.randint(1, 1000000) for i in range(100000)]
i = 50000

value, time_taken = timed_randomized_select(A, i)

print("i-th smallest:", value)
print("Time taken:", time_taken, "seconds")