from timeit import Timer

size = 1000

def test1(): #concatenation
    the_list = []
    for i in range(size):
        the_list = the_list + [i]

def test2(): #appending
    the_list = []
    for i in range(size):
        the_list.append(i)

def test3(): #list comprehension
    the_list = [i for i in range(size)]

def test4(): #list range
    the_list = list(range(size))


t1 = Timer("test1()", "from __main__ import test1")
print(f"concatenation: {t1.timeit(number=1000):15.2f} milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print(f"appending: {t2.timeit(number=1000):19.2f} milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print(f"list comprehension: {t3.timeit(number=1000):10.2f} milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print(f"list range: {t4.timeit(number=1000):18.2f} milliseconds")