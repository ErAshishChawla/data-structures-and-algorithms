import math

def isArmstrongNumber(n:int) -> bool:
    if n < 0:
        return False

    if n == 0:
        return True
    
    length = int(math.log10(n) + 1)
    num = n
    total = 0

    while num > 0:
        total = total + ((num % 10) ** length)
        num = num // 10

    return total == n


print(isArmstrongNumber(153))
print(isArmstrongNumber(370))
print(isArmstrongNumber(9474))
print(isArmstrongNumber(0))




    