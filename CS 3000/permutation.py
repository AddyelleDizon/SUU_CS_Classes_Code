import random
import matplotlib.pyplot as plt

def random_shuffle(A):
    n = len(A)
    for i in range(n):
        j = random.randint(i, n - 1)
        A[i], A[j] = A[j], A[i]

def permute_with_all(A):
    n = len(A)
    for i in range(n):
        j = random.randint(0, n - 1)
        A[i], A[j] = A[j], A[i]

def test(randomizer, trials):
    counts = {}

    for i in range(trials):
        A = ['A', 'B', 'C', 'D', 'E']
        randomizer(A)
        perm = ''.join(A)

        if perm in counts:
            counts[perm] += 1
        else:
            counts[perm] = 1

    return counts

trials = 10000000

r1 = test(random_shuffle, trials)
r2 = test(permute_with_all, trials)

print("random shuffle:")
for k in list(r1)[:10]:
    print(k, r1[k])

print("\npermute with all:")
for k in list(r2)[:10]:
    print(k, r2[k])

perms = sorted(r1.keys())
r1_vals = [r1[p] for p in perms]
r2_vals = [r2[p] for p in perms]

# random shuffle graph
plt.figure()
plt.bar(range(len(r1_vals)), r1_vals)
plt.title("Random Shuffle")
plt.xlabel("Permutation index")
plt.ylabel("Count")
plt.show()

# permute with all graph
plt.figure()
plt.bar(range(len(r2_vals)), r2_vals)
plt.title("Permute With All")
plt.xlabel("Permutation index")
plt.ylabel("Count")
plt.show()