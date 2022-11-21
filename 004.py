"""
Write a function called check_duplicates that takes a list of 
strings as an argument. The function should check if the list has 
any duplicates. If there are duplicates, the function should return 
the duplicates. If there are no duplicates, the function should 
return "No duplicates". For example, the list of fruits below 
should return apple as a duplicate and list of names should 
return "no duplicates".
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
"""


def check_duplicates(words):
    """
    takes a list of strings as an argument and checks if the list has 
    any duplicates. If there are duplicates, the function should return 
    the duplicates. If there are no duplicates, the function should 
    return "No duplicates".
    
    Args:
        words (list(strings))

    Return
        list of duplicates - list(string)
    """
    map = {}
    for i in words:
        # https://www.educative.io/answers/how-to-check-if-a-key-exists-in-a-python-dictionary
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    results = []    
    for i in map.keys():
        if map[i] > 1:
            results.append(i)
    if results:
        return results

    return "no duplicates"    


def validation_004(func, input, validate_value):
    """
    Validate the function to see if passes validation testing
    
    Args:
        func (function)
        input (list(string))
        validation_value (list)

    return
        boolean - if function passes validation
    """

    return (func(input) == validate_value)


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
# print(check_duplicates(fruits))
# print(check_duplicates(names))

print(validation_004(check_duplicates, fruits, ['apple']))
print(validation_004(check_duplicates, names, 'no duplicates'))