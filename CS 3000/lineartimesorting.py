import random
import time
import matplotlib.pyplot as plt

def insertion_sort_points(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort_points(points):
    n = len(points)
    if n == 0:
        return points

    buckets = [[] for _ in range(n)]

    for p in points:
        index = int(n * p[0])
        buckets[index].append(p)

    for b in buckets:
        insertion_sort_points(b)

    k = 0
    for b in buckets:
        for p in b:
            points[k] = p
            k += 1

    return points

def generate_unit_square_points(n):
    return [(random.random(), random.random()) for i in range(n)]

def time_bucket_sort_points(n):
    points = generate_unit_square_points(n)

    startTime = time.time()
    bucket_sort_points(points)
    endTime = time.time()

    return endTime - startTime

sizes = [10, 100, 1000, 100000, 10000000]
times = []

for n in sizes:
    print(f"Running n = {n}")
    t = time_bucket_sort_points(n)
    times.append(t)
    print(f"Time: {t:.6f} seconds\n")

plt.figure()
plt.plot(sizes, times, marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Bucket Sort Runtime")
plt.grid(True)
plt.show()