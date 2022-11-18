"""
Day 1: Division and Square-root
Write a function called divide_or_square that takes one 
argument (a number), and returns the square root of the number 
if it is divisible by 5, returns its remainder if it is not divisible by 
5. For example, if you pass 10 as an argument, then your function 
should return 3.16 as the square root
"""
from math import sqrt

def divide_or_square(number):
    """
    function takes one argument (a number), and 
    returns the square root of the number 
    if it is divisible by 5, 
    returns its remainder if it is not divisible by 5. 

    Args:
        number (int)

    returns
        float 
    """

    if (number % 5):
        return number % 5
    return sqrt(number)



# look into using **args for multiple input values
def validation_001(func, input, validate_value):
    """
    Validate the function to see if passes validation testing
    
    Args:
        func (function)
        input (args for function)
        validation_value (float)

    return
        boolean - if function passes validation
    """

    return (round(func(input),2) == validate_value)



print(validation_001(divide_or_square, 10, 3.16))