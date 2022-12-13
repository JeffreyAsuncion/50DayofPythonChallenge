"""
Extra Challenge: Swap Values
Write a function called swap_values. This function takes a list 
of numbers and swaps the first element with the last element. 
For example, if you pass [2, 4,67, 7] as a parameter, your 
function should return
[7, 4, 67, 2].
"""


def swap_values(nums):
    """
    takes a list of numbers and swaps the first element with the last element

    Args
        nums (list[int]) - list of nums

    Return
        list[int]
    """
    nums[0], nums[-1] = nums[-1], nums[0]

    return nums


nums = [2, 4,67, 7]
print(swap_values(nums))