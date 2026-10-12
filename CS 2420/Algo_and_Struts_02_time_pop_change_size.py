from timeit import Timer

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

print(f"{'n':10s}{'pop(0)':>15s}{'pop()':>15s}")

for i in range(1_000_000, 50_000_001, 1_000_000):
    x = list(range(i))
    pop_zero_t = pop_zero.timeit(number=5)
    x = list(range(i))
    pop_end_t = pop_end.timeit(number=1000)
    print(f"{i:<10d}{pop_zero_t:>15.5f}{pop_end_t:>15.5f}")
