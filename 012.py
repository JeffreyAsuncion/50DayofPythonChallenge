"""
Extra Challenge: Zero Both ends
Write a function called zeroed code that takes a list of numbers 
as an argument. The code should zero (0) the first and the last 
number in the list. For example, if the input is [2, 5, 7, 8, 9],
your code should return [0, 5, 7, 8, 0]
"""

def zeroed(nums):
    nums[0] = nums[-1] = 0
    return nums

nums = [2, 5, 7, 8, 9]
print(zeroed(nums))