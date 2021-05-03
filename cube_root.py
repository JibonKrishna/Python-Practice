"""
Created on Tuesday, October 27, 2020

@author: Jibon_Krishna
"""


# cube root of a positive number using bisection search.
# assumes x is positive

x = float(input("Enter a positive number: "))
num_guesses = 0
ans = 0
high = 0
low = 0

if x < 1:
    high = 1
else:
    high = x

while abs((ans**3) - abs(x)) > 0.01:
    num_guesses += 1
    ans = (high + low) / 2
    if ans**3 > x:
        high = ans
    else:
        low = ans
print(f"Cube root of {x} is {ans}.")
print(f"It took {num_guesses} guesses.")
