"""
Day 8: Odd and Even
Write a function called odd_even that has one parameter and
takes a list of numbers as an argument. The function returns the 
difference between the largest even number in the list and the 
smallest odd number in the list. For example, if you pass 
[1,2,4,6] as an argument the function should return 6 -1= 5.
"""


def odd_even(nums):
    nums.sort()
    highest_even = nums[0]
    lowest_odd = nums[0]

    for i in range(len(nums)):
        
        if (not(nums[i]) % 2):
            if nums[i] > highest_even:
                highest_even = nums[i]
            
        if (nums[i]) % 2:
            if nums[i] < lowest_odd:
                lowest_odd = nums[i]
                print(lowest_odd)
    return highest_even - lowest_odd


nums = [1,2,4,6]
print(odd_even(nums))