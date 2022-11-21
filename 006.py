"""
Extra Challenge: Lowercase Names
 
names = ["kerry", "dickson", "John", "Mary", 
 "carol", "Rose", "adam"]
You are given a list of names above. This list is made up of names 
of lowercase and uppercase letters. Your task is to write a code 
that will return a tuple of all the names in the list that have only
lowercase letters. Your tuple should have names sorted 
alphabetically in descending order. Using the list above, your 
code should return:
('kerry', 'dickson', 'carol', 'adam')
"""


# print(("A").islower(), "a".islower())
def check_all_lowercase(names):
    """
    return a tuple of all the names in the list 
    that have only lowercase letters

    Args:
        names (list(strings))
    
    Return
        tuple of lowercase names
    """
    lowercase_names = []
    for word in names:
        count = 0
        for letter in word:
            if letter.isupper():
                count += 1
        if not count:
            lowercase_names.append(word)
    return tuple(lowercase_names)


def validation_006(func, input, validate_value):
    """
    Validate the function to see if passes validation testing
    
    Args:
        func (function)
        input (list(string))
        validation_value (list(string))

    return
        boolean - if function passes validation
    """

    return (func(input) == validate_value)


names = ["kerry", "dickson", "John", "Mary", 
 "carol", "Rose", "adam"]

print(check_all_lowercase(names))
validate_value = ('kerry', 'dickson', 'carol', 'adam')
print(validation_006(check_all_lowercase, names, validate_value))