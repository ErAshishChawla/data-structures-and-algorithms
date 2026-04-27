def fib(n):
    fib_map = {
        0:0,
        1:1
    }

    for i in range(2, n+1):
        fib_map[i] = fib_map[i-1] + fib_map[i-2]

    return fib_map[n]

print(fib(7))