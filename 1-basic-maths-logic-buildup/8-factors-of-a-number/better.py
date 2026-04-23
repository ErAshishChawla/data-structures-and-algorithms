def factors(n:int):
    factors = [1, n]

    for i in range(2, n // 2  + 1):
        if n % i == 0:
            factors.append(i)

    return factors


print(factors(12))
print(factors(20))