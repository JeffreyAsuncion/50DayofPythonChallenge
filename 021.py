"""
Day 11: Are They Equal?
Write a function called equal_strings. The function takes two 
strings as arguments and compares them. If the strings are equal 
(if they have the same characters and have equal length), it 
should return True, if they are not, it should return False. For 
example, ‘love’ and ‘evol’ should return True.
"""



def equal_strings(word1, word2):
    """
     takes two strings as arguments and compares them. 
     If the strings are equal 
    (if they have the same characters and have equal length), 
    it should return True, if they are not, it should return False.

    Args
        word1 (str)
        word2 (str)

    Return
        boolean
    """
    
    word1s = sorted(word1)
    word2s = sorted(word2)

    if word1s == word2s and len(word1) == len(word2):
        return True

    return False


word1 = 'love'
word2 = 'evol'

print(equal_strings(word1, word2))