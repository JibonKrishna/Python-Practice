"""
Created on Tuesday, November 03, 2020

@author: Jibon_Krishna
"""


def WordCount(word, string):
    """Counts the number of time a word found in a input string.

    Args:
        word (str): The word to count.
        string (str): The string.
    """
    word_count = 0
    for i in range(0, len(string)-2):
        if string[i:i+3] == word:
            word_count += 1
    return word_count


string = str(input("Enter a string: "))
word = str(input("Enter the word to count: "))
word_count = WordCount(word, string)
if word_count < 2:
    print(
        f"The word \"{word}\" repeated {word_count} time in the input string.")
else:
    print(
        f"The word \"{word}\" repeated {word_count} times in the input string.")
