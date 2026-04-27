def isPalindrome(s:str, l:int, r:int):
    if l > r:
        return True
    

    if s[l] != s[r]:
        return False

    return isPalindrome(s, l + 1, r - 1)
str1 = "abba"
str2 = "abbab"
print(isPalindrome(str1, 0, len(str1) - 1))
print(isPalindrome(str2, 0, len(str2) - 1))
