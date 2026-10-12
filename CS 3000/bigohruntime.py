import time
import random
import matplotlib.pyplot as plt

startTime = time.time()

digits = []
mult_times = []
div_times = []

for n in range(1, 20000, 500):
    a = random.randint(10**(n - 1), 10**n - 1)
    b = random.randint(10**(n - 1), 10**n - 1)

    start = time.time()
    a * b
    mult_time = time.time() - start

    start = time.time()
    a / b
    div_time = time.time() - start

    digits.append(n)
    mult_times.append(mult_time)
    div_times.append(div_time)

    print("digits:", n,
          " multiply:", mult_time,
          " divide:", div_time)

endTime = time.time()
totalTime = endTime - startTime
print("Total program time:", totalTime)

plt.figure()
plt.plot(digits, mult_times, label="Multiplication")
plt.plot(digits, div_times, label="Division (/)")
plt.xlabel("Number of digits (n)")
plt.ylabel("Time (seconds)")
plt.title("Runtime of Big Integer Arithmetic")
plt.legend()
plt.show()