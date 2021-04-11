"""
Created on Sunday, April 11, 2021

@author: Jibon_Krishna
"""


# counts the number of lines in a text file

# open file
file = open("words.txt", "r")

# Reads the input text file and converts the lines to a list
read_file = file.read()
line_list = read_file.split("\n")


print("This is the number of lines in the file")
print(len(line_list))
