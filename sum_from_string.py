"""
Created on Wednesday, October 28, 2020

@author: Jibon_Krishna
"""


def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    sum = 0
    for i in range(0, len(s)):
        if s[i] in digits:
            sum += int(s[i])
    return sum


x = str(input("Enter a string: "))
print(f"Sum of the decimal digits in your input:", sumDigits(x))
