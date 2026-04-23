def factors(n:int):
    if n == 0:
        return []

    factors = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            other_factor = n // i
            if other_factor != i:
                factors.append(other_factor)
    
    return factors

print(factors(12))
print(factors(100))

