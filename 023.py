"""
Day 12: Count the Dots
Write a function called count_dots. This function takes a 
string separated by dots as a parameter and counts how many 
dots are in the string. For example, ‘h.e.l.p.’ should return 4
dots, and ‘he.lp.’ should return 2 dots.
"""


def count_dots(word):
    """
    takes a string separated by dots as a parameter 
    and counts how many dots are in the string.

    Args
        word (str)

    Return
        int
    """
    return word.count('.')

word1 = 'h.e.l.p.'
word2 = 'he.lp.'

print(count_dots(word1))
print(count_dots(word2))