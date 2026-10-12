from timeit import Timer

for size in sizes:
        dct = data[f"dict_{size}"]
        indices = random.sample(range(size), 1000)

        # Measure time for setting
        set_timer = Timer(lambda: [dct.__setitem__(idx, 42) for idx in indices])
        set_time = set_timer.timeit(number=1)

        # Measure time for getting
        get_timer = Timer(lambda: [dct.__getitem__(idx) for idx in indices])
        get_time = get_timer.timeit(number=1)

        print(f"Dict size {size}: set_time={set_time:.6f}, get_time={get_time:.6f}")