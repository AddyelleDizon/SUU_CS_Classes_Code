import random
import matplotlib.pyplot as plt

def makeIntArrayForMaxSubArray(size):
    a = []
    for i in range(size):
        a.append(random.randint(-20,20))
    return a

def bruteForce(A):
    low = high = 0
    max_sum = A[0]

    n = len(A)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += A[j]
            if current_sum > max_sum:
                max_sum = current_sum
                low = i
                high = j

    return low, high, max_sum

def findMaxCrossingSubarray(A, low, mid, high):
    sum = 0
    left_sum = A[mid]
    max_left = mid

    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    sum = 0
    right_sum = A[mid + 1]
    max_right = mid + 1

    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum

def findMaximumSubarray(A, low, high):
    if low == high:
        return low, high, A[low]

    mid = (low + high) // 2

    left_low, left_high, left_sum = findMaximumSubarray(A, low, mid)
    right_low, right_high, right_sum = findMaximumSubarray(A, mid + 1, high)
    cross_low, cross_high, cross_sum = findMaxCrossingSubarray(A, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


# Testing

import time

sizes = list(range(20, 401, 20))
bf_times = []
rec_times = []
hyb_times = []


for n in sizes:
    A = makeIntArrayForMaxSubArray(n)

    start = time.time()
    bruteForce(A)
    bf_times.append(time.time() - start)

    start = time.time()
    findMaximumSubarray(A, 0, n - 1)
    rec_times.append(time.time() - start)


n0 = None
for i in range(len(sizes)):
    if rec_times[i] < bf_times[i]:
        n0 = sizes[i]
        break

print("Crossover point n₀ =", n0)

def hybridWrapper(A, low, high):
    if high - low + 1 <= n0:
        return bruteForce(A[low:high+1])
    return findMaximumSubarray(A, low, high)

for n in sizes:
    A = makeIntArrayForMaxSubArray(n)

    start = time.time()
    hybridWrapper(A, 0, n - 1)
    hyb_times.append(time.time() - start)


plt.plot(sizes, bf_times, marker='o', label='Brute Force O(n²)')
plt.plot(sizes, rec_times, marker='s', label='Recursive O(n log n)')
plt.plot(sizes, hyb_times, marker='^', label='Hybrid')

plt.axvline(n0, linestyle='--', label=f'Crossover n₀ ≈ {n0}')

plt.xlabel("Input Size n")
plt.ylabel("Runtime (seconds)")
plt.title("Maximum Subarray Crossover Analysis")
plt.legend()
plt.grid(True)
plt.show()