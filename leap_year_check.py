"""
Created on Monday, October 26, 2020

@author: Jibon_Krishna
"""


def is_leap(x):
    """Checks whether a year is leap year or not.

    Args:
        x (int): Year, a decimal integer.

    Returns:
        bool: True if the input is a leap year and false otherwise.
    """
    if x % 4 == 0:
        leap = True
        if x % 100 == 0:
            leap = False
            if x % 400 == 0:
                leap = True
        else:
            leap = true
    else:
        leap = False
    return leap


year = int(input("Input a year: "))
check = is_leap(year)
if check == True:
    print(year, "is a leap year.")
if check == False:
    print(year, "is not a leap year.")
