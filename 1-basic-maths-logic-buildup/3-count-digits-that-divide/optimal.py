def evenlyDivides(n: int):
    count = 0
    num = n

    while num > 0:
        last_digit = num % 10
        if last_digit > 0 and n % last_digit == 0:
            count += 1
        num = num // 10

    return count
