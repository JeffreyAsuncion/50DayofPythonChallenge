"""
Write a function called only_floats, which takes two 
parameters a and b, and returns 2 if both arguments are floats,
returns 1 if only one argument is a float, and returns 0 if neither 
argument is a float. If you pass (12.1, 23) as an argument, your 
function should return a 1.
"""

def only_floats(numbers):
    """
    returns the number of floats

    Args:
        numbers (tuple of numbers)

    Return
        int
    """
    count = 0
    for i in numbers:
        if isinstance(i, float):
            count +=1
    return count

def validation_007(func, input, validate_value):
    """
    Validate the function to see if passes validation testing
    
    Args:
        func (function)
        input (tuple(nums))
        validation_value (int)

    return
        boolean - if function passes validation
    """

    return (func(input) == validate_value)


input_tuple = (12.1, 23)
# print(only_floats(input_tuple))
validate_value=1

print(validation_007(only_floats, input_tuple, validate_value))
