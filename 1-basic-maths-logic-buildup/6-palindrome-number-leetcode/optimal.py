def isPalindrome(n:int) -> bool:
    if n < 0:
        return False

    if n < 10:
        return True

    num = n
    reverse = 0
    while num > 0:
        reverse = reverse * 10 + num % 10
        num = num // 10

    return reverse == n