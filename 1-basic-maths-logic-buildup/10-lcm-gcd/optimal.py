def lcmGcd(a: int, b: int):
    if a == 0 and b == 0:
        return {"lcm": 0, "gcd": 0}
    elif a == 0 or b == 0:
        return {"lcm": 0, "gcd": max(a, b)}
    elif a == 1 or b == 1:
        return {"lcm": a * b, "gcd": 1}
    
    dividend, divisor = max(a,b), min(a,b)

    while divisor != 0:
        rem = dividend % divisor
        dividend = divisor
        divisor = rem

    gcd = dividend
    lcm = (a*b) // gcd

    return {"lcm": lcm, "gcd": gcd}


print(lcmGcd(12, 18))  # 36, 6
print(lcmGcd(12, 30))  # 60, 6
print(lcmGcd(7, 11))   # 77, 1
print(lcmGcd(0, 5))    # 0, 5

