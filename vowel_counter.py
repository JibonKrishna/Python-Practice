"""
Created on Friday, November 27, 2020

@author: Jibon_Krishna
"""

# Takes a string as input and prints the number of vowels in the input string.

# converts the input string to a list of unique characters
string = list(set(input("Enter your string: ").lower()))


vowel = ['a', 'e', 'i', 'o', 'u']
count = 0


for letter in string:
    if letter in vowel:
        count += 1


# Singular-plural
if count > 1:
    print(f"There are {count} vowels in your input.")
else:
    print(f"There is only {count} vowel in your input.")
