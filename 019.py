"""
Day 10: Hide my Password
Write a function called hide_password that takes no 
parameters. The function takes an input (a password) from a 
user and returns a hidden password. For example, if the user 
enters ‘hello’ as a password the function should return ‘****’ as 
a password and tell the user that the password is 4 characters
long.
"""

password = input("Please enter your password : ")

pw_length = len(set(password))

print(pw_length * '*', pw_length)