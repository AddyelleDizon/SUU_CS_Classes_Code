import random

def furthest_in_future(requests, k):
    cache = []
    misses = 0
    decisions = []

    for i in range(len(requests)):
        r = requests[i]

        if r in cache:
            decisions.append(f"Request {r}: HIT")
            continue

        misses += 1

        if len(cache) < k:
            cache.append(r)
            decisions.append(f"Request {r}: MISS, added to cache")
            continue

        future = requests[i+1:]

        furthest_index = -1
        evict_item = None

        for item in cache:
            if item in future:
                next_use = future.index(item)
            else:
                next_use = float('inf')

            if next_use > furthest_index:
                furthest_index = next_use
                evict_item = item

        cache.remove(evict_item)
        cache.append(r)

        decisions.append(f"Request {r}: MISS, evict {evict_item}")

    return decisions, misses


def run_trial():
    requests = [random.randint(0,20) for _ in range(50)]
    decisions, misses = furthest_in_future(requests, 10)

    print("Requests:")
    print(requests)
    print("\nTotal Misses:", misses)
    print("Total Hits:", 50 - misses)
    print("-" * 40)

for i in range(3):
    print(f"Trial {i+1}")
    run_trial()