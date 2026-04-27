def fib(n:int):
    if n == 0 or n== 1:
        return n

    one = 0
    two = 1

    for i in range(2, n  + 1):
        three = one + two
        one = two
        two = three

    return two

print(fib(7))