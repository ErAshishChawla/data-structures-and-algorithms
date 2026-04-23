def printFactors(n:int):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

printFactors(1232)