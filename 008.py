"""
Write a function called word_index that takes one argument, 
a list of strings and returns the index of the longest word in the 
list. If there is no longest word (if all the strings are of the same 
length), the function should return zero (0). For example, the list 
below should return 2.
words1 = ["Hate", "remorse", "vengeance"]
 And this list below, shoul return zero (0)
words2 = ["Love", "Hate"]
"""


def word_index(words):
    """
    returns the index of the longest word in the list. 
    If there is no longest word (if all the strings are 
    of the same length), the function should return zero (0)

    Args:
        word (list(string))

    Return
        int or list(string())
    """
    map = {}
    longest = 0
    longest_word_list = []

    for i in words:
        map[i] = len(i)
        if map[i] > longest:
            longest = map[i]

    for i in words:
        if map[i] == longest:
            longest_word_list.append(i)

    if len(longest_word_list) > 1:
        return longest_word_list
    
    return 1


def find_longest_word(words):
    map = {}
    for i in words:
        map[i] = len(i)

    longest = 0
    longest_word_list = []
    for i in map.keys():
        if map[i] > longest:
            longest = map[i]

    for i in words:
        if map[i] == longest:
            longest_word_list.append(i)

    if len(longest_word_list) > 1:
        return longest_word_list
    
    return 1

def validation_008(func, input, validate_value):
    """
    Validate the function to see if passes validation testing
    
    Args:
        func (function)
        input (list[str])
        validation_value (dict)

    return
        boolean - if function passes validation
    """

    return (func(input) == validate_value)

words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

# print(find_longest_word(words1))
# print(find_longest_word(words2))

# print(word_index(words1))
# print(word_index(words2))

validate1 = 1
validate2 = ['Love', 'Hate']

print(validation_008(word_index, words1, validate1))
print(validation_008(word_index, words2, validate2))