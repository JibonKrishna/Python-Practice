"""
Created on Sunday, October 25, 2020

@author: Jibon_Krishna
"""


# generates random number and writes into the "numbers" file.
import random
n = int(input("Number of random number you want to generate: "))
print("\nRange")
start = int(input("\tFrom: "))
end = int(input("\tTo: "))
x = open('numbers', 'w')
for i in range(n):
    number = random.randint(start, end)
    x.write(str(number))
x.close()
print("Completed!")
