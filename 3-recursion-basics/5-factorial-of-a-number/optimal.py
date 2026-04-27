def factorial(n:int) -> int:
    acc = 1

    for val in range(1 , n + 1):
        acc= acc * val
    
    return acc

print(factorial(5))