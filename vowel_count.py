"""
Created on Friday, November 27, 2020

@author: Jibon_Krishna
"""


string = str(input("Input a string: ").lower())
count = 0
vowel = ['a', 'e', 'i', 'o', 'u']

for letter in string:
    if letter in vowel:
        count += 1
print(f"There are {count} vowels in your input string")
