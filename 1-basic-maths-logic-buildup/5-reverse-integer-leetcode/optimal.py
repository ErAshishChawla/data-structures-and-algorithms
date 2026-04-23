def reverse(n:int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    num = abs(n)

    if num == 0:
        return 0

    reverse = 0

    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num = num // 10

    reverse = -1 * reverse if n < 0 else reverse

    if reverse > INT_MAX or reverse < INT_MIN:
        return 0

    return reverse

print(reverse(123))
print(reverse(-123))
print(reverse(120))