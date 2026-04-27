def headRecursion(i:int, n:int):
    if i > n:
        return
    
    headRecursion(i + 1, n)
    print(i)

def tailRecursion(n:int):
    if n <=0:
        return 
    
    print(n)
    tailRecursion(n - 1)

headRecursion(1, 10)
tailRecursion(10)
