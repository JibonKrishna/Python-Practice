"""
Created on Tuesday, October 27, 2020

@author: Jibon_Krishna
"""


# cube root of positive number using bisection search
x = float(input("enter a number: "))
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
print(ans)
print(num_guesses)
