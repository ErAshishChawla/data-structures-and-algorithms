def headRecursion(n):
    #base case
    if n <=0:
        return
    
    # recursion
    headRecursion(n-1)
    print(n)

headRecursion(10)

print("-----------------------------")

def tailRecursion(i, n):
    # base case
    if i > n:
        return

    # Work
    print(i)

    # Recursive call
    tailRecursion(i + 1, n)

tailRecursion(1, 10)
