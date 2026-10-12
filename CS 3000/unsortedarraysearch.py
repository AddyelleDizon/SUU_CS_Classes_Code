import random

def random_search(A, x):
    n = len(A)
    checked = [False] * n
    checked_count = 0

    while checked_count < n:
        i = random.randrange(n)

        if not checked[i]:
            checked[i] = True
            checked_count += 1

            if A[i] == x:
                return i

    return None

def deterministic_search(A, x):
    n = len(A)

    for i in range(n):
        if A[i] == x:
            return i

    return None

def scramble_search(A, x):
    B = A.copy()
    random.shuffle(B)

    for i in range(len(B)):
        if B[i] == x:
            return i

    return None


def record_and_display_data(A, iterations):
    total_random = total_det = total_scramble = 0
    n = len(A)

    for i in range(iterations):
        x = random.choice(A)

        # random search
        checked = [False] * n
        checked_count = 0
        checks = 0
        while checked_count < n:
            i = random.randrange(n)
            checks += 1
            if not checked[i]:
                checked[i] = True
                checked_count += 1
                if A[i] == x:
                    break
        total_random += checks

        # deterministic search
        checks = 0
        for i in range(n):
            checks += 1
            if A[i] == x:
                break
        total_det += checks

        # scramble search
        B = A.copy()
        random.shuffle(B)
        checks = 0
        for i in range(n):
            checks += 1
            if B[i] == x:
                break
        total_scramble += checks

    # print data
    print("Average checks:")
    print("Random-Search:", total_random / iterations)
    print("Deterministic-Search:", total_det / iterations)
    print("Scramble-Search:", total_scramble / iterations)

A = [random.randint(0, 1000) for i in range(10000)]
record_and_display_data(A, 10000)