def isPalindrome(s:str):
    l = 0
    r = len(s)-1

    while l<r:
        if s[l] !=s[r]:
            return False
        l = l+1
        r = r-1

    return True


str1 = "abba"
str2 = "abbab"
print(isPalindrome(str1))
print(isPalindrome(str2))
