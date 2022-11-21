"""
Write a function called register_check that checks how many 
students are in school. The function takes a dictionary as a 
parameter. If the student is in school, the dictionary says ‘yes’. If 
the student is not in school, the dictionary says ‘no’. Your 
function should return the number of students in school. Use the 
dictionary below. Your function should return 3.
register = {'Michael':'yes','John': 'no', 
 'Peter':'yes', 'Mary': 'yes'}
"""

def register_check(student_dict):
    """
    checks how many students are in school.

    Args:
        student_dict (dict)

    Return
        int - number of students in school
    """
    count = 0

    for i in student_dict.keys():
        if student_dict[i] == 'yes':
            count += 1
    
    return count


def validation_005(func, input, validate_value):
    """
    Validate the function to see if passes validation testing
    
    Args:
        func (function)
        input (dict)
        validation_value (int)

    return
        boolean - if function passes validation
    """

    return (func(input) == validate_value)



register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}

# print(register_check(register))
print(validation_005(register_check, register, 3))