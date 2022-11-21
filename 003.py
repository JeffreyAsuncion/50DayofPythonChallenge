"""
Write a function called convert_add that takes a list of strings 
as an argument and converts it to integers and sums the list. For 
example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
summed to 9
"""

def convert_add(numbers):
    """
    Takes a list of strings as an argument 
    and converts it to integers and sums the list.

    Args:
    numbers (list(int))

    return
    int - sum of list of ints 
    """
    new_list = []
    for i in numbers:
        new_list.append(int(i))
    return sum(new_list)

def validation_003(func, input, validate_value):
    """
    Validate the function to see if passes validation testing
    
    Args:
        func (function)
        input (list(char))
        validation_value (int)

    return
        boolean - if function passes validation
    """

    return (func(input) == validate_value)

a = ['1', '3', '5']
# print(convert_add(a))

print(validation_003(convert_add, a, 9))