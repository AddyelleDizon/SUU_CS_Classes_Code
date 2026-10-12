memory = [0]*101
def fib(n):
    if memory[n] != 0:
        return memory[n]
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        ans = fib(n-1) + fib(n-2)
        memory[n] = ans
        return ans
    
for i in range(1, 100):
    print(i, "=", fib(i))