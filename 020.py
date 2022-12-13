"""
Extra Challenge: A Thousand Separator
Your new company has a list of figures saved in a list. The issue 
is that these numbers have no separator. The numbers are 
saved in the following format:
[1000000, 2356989, 2354672, 9878098].

You have been asked to write a code that will convert each of the 
numbers in the list into a string. Your code should then add a 
comma on each number as a thousand separator for 
readability. When you run your code on the above list, your 
output should be:
[ '1,000,000', '2,356,989', '2,354,672', '9,878,098’]
Write a function called convert_numbers that will take one 
argument, a list of numbers above.
"""

def convert_numbers(list_of_nums):
    list_of_str = []
    for i in list_of_nums:   
        list_of_str.append(str(i))

    # print(len(list_of_str))
    list_thousands = []
    
    for i in range(len(list_of_str)):
        num_str = ''
        x = len(list_of_str[i])
        
        a = x % 3
        thousands = x // 3
        
        # add the first part before the first thousands place
        if a > 0:
            num_str += list_of_str[i][:a] + ','


        # after first comma
        for j in range(thousands):     
            num_str +=  list_of_str[i][a:a+3] + ','
            a += 3

        list_thousands.append(num_str[:-1])
    
    return list_thousands


list_of_nums = [1000000, 2356989, 2354672, 9878098, 111222333444555666777]
print(convert_numbers(list_of_nums))