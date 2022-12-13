"""
Day 9: Biggest Odd Number
Create a function called biggest_odd that takes a string of 
numbers and returns the biggest odd number in the list. For 
example, if you pass ‘23569’ as an argument, your function 
should return 9. Use list comprehension.
"""

def biggest_odd_ver1(str_of_nums):
    # str_of_nums = '23569'
    biggest = 0

    for i in str_of_nums:
        if int(i) % 2: 
            if int(i) > biggest:
                biggest = int(i)

    return biggest

str_of_nums = '23569'
biggest = 0

print([int(i) for i in str_of_nums if int(i) % 2][-1])
            
