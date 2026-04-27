def func(n:int):
    acc = 0

    for val in range(1, n + 1):
        acc = acc + val
    
    return acc

print(func(5))