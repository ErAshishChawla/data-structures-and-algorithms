def extractDigits(n: int):
    num = abs(n)

    if num == 0:
        print(num, end=" ")

    while num > 0:
        last_digit = num % 10
        print(last_digit, end=" ")
        num = num // 10

    print()
    return


extractDigits(5873)
extractDigits(0)
extractDigits(-1343)
