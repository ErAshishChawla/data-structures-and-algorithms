def buySellStock(arr):
    n = len(arr)
    buy = 0
    max_profit = 0
    
    for sell in range(n):
        profit = arr[sell] - arr[buy]
        max_profit = max(max_profit, profit)

        if profit < 0:
            buy = sell

    return max_profit


arr = [7,1,5,3,6,4]
print(buySellStock(arr))