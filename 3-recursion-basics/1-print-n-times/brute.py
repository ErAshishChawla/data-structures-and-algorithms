def func(n:int):
    if n <= 0:
        return
        
    print("Hello World")
    func(n-1)

func(5)