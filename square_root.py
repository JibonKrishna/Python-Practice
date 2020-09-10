# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 23:03:05 2020

@author: jibon_k
"""
# find square root of a number by bisection search.

x = int(input("Enter the number: "))
low = 0
high = x
num_guesses = 0
ans = (high + low) / 2

while abs(ans**2 - x) >= 0.1:
    num_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print(f"\nSquare root of {x} is {ans}.")
print(f"\nIt took {num_guesses} guesses.")
