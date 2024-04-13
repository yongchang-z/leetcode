"""
Given an integer x, return True if x is a palindrome, and false otherwise."""

# Intuitive Solution
def isPalindrome(x):
    if x < 0:
        return False
    
    low = 0
    high = len(str(x)) - 1

    while low < high:
        if str(x)[low] != str(x)[high]:
            return False
        low += 1
        high -= 1
    return True

# Optimized Solution
def isPalindrome_optimized(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

# Solution directly manipulates the digits
def isPalindrome_direct(x):
    if x < 0:
        return False

    reversed = 0
    original = x
    while x:
        digit = x % 10
        reversed = reversed * 10 + digit
        x //= 10
    return reversed == original


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(1001))
print(isPalindrome(0))