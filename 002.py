"""
Extra Challenge: Longest Value
Write a function called longest_value that takes a dictionary 
as an argument and returns the first longest value of the 
dictionary. 
For example, the following dictionary should return 
– apple as the longest value.
fruits = {'fruit': 'apple', 'color': 'green'}
"""
def longest_value(input_dict):
    """
    
    """
    map = {}
    longest = ''
    for i in input_dict.values():
        if len(i) > len(longest):
            longest = i
    
    return longest

def validation_002(func, input, validate_value):
    """
    Validate the function to see if passes validation testing
    
    Args:
        func (function)
        input (dict)
        validation_value (string)

    return
        boolean - if function passes validation
    """

    return (func(input) == validate_value)


fruits = {'fruit': 'apple', 'color': 'green'}
# print((longest_value(fruits))=='apple')
print(validation_002(longest_value, fruits, 'apple'))