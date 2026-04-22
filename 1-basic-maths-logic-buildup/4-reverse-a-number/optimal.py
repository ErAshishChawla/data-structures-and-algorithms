def reverseNumber(n:int):
    num = abs(n)
    reverse = 0

    if num == 0:
        return 0

    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num = num // 10

    return -1 * reverse if n < 0 else reverse

print(reverseNumber(1000))
print(reverseNumber(2050))
print(reverseNumber(1))
print(reverseNumber(0))
print(reverseNumber(-1000))
print(reverseNumber(-427994))