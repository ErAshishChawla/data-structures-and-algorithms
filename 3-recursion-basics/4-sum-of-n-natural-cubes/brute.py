def func(n:int):
    if n == 1:
        return 1

    return n**3 + func(n-1)

print(func(5))