import math as m


def countDigits(n: int):
    num = abs(n)

    if num == 0:
        return 1

    return int(m.log10(num) + 1)


print(countDigits(2423))
print(countDigits(0))
print(countDigits(1))
print(countDigits(-134324))
