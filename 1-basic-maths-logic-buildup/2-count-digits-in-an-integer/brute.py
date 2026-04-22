def countDigits(n: int):
    num = abs(n)

    if num == 0:
        return 1

    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    return count


print(countDigits(2423))
print(countDigits(00))
print(countDigits(-134324))
