"""
Created on Thursday, October 29, 2020

@author: Jibon_Krishna
"""


def largest(s):
    """Takes sequence of numbers separated by comma as input and returns
    the largest number. If the input is "1.2,1,5,2,4,5.2,1,5", it will
    return 5.2

    Args:
        s (str): A sequence of number separated by comma.
    """
    x = s.split(",")
    i = 0
    largest = 0
    try:
        while i+1 < len(x) and len(x) > 1:
            if largest < float(x[i]) and\
                    float(x[i]) > float(x[i+1]):
                largest = float(x[i])
            elif float(x[i+1]) > largest:
                largest = float(x[i+1])
            i += 1
        if len(x) == 1:
            largest = float(x[0])
        return largest
    except ValueError:
        print("\n\tWrong input! \n")


number = str(input("Enter a sequence of number separated by comma: "))
if largest(number) != None:
    print(f"The largest number of the sequence is {largest(number)}.")
