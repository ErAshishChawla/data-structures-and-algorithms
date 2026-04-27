def isPalindrome(s:str):
    rev_str = s[::-1]

    return rev_str == s

print(isPalindrome("abba"))
print(isPalindrome("abbab"))