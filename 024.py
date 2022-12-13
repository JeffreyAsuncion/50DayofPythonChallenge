"""
Extra Challenge: Your Age in Minutes
Write a function called age_in_minutes that tells a user how 
old they are in minutes. Your code should ask the user to 
enter their year of birth, and it should return their age in 
minutes (by subtracting their year of birth to the current year). 
Here are things to look out for:
a. The user can only input a 4-digit year of birth. For 
example, 1930 is a valid year. However, entering any 
number longer or less than 4 digits long should render 
input invalid. Notify the user to input a four digits 
number.
b. If a user enters a year before 1900, your code should 
tell the user that input is invalid. If the user enters the 
year after the current year, the code should tell the user, 
to input a valid year.
The code should run until the user inputs a valid year. 
Your function should return the user's age in minutes. For 
example, if someone enters 1930, as their year of birth your 
function should return:
You are 48,355,200 minutes old
"""
from datetime import date

def age_in_minutes(birth_year):
    """
    ask the user to enter their year of birth, 
    and it should return their age in minutes 
    (by subtracting their year of birth to the current year)

    Args
        birth_year(int)
    Return

    """
    if birth_year < 1900 or birth_year > 9999:
        print("Error, Invalid Year!!!")
        return -1
    current_year = date.today().year
    diff_year = current_year - birth_year
    year_in_mins = diff_year * 365 * 24 * 60

    return year_in_mins

birth_year1 = 1899
birth_year2 = 1930
birth_year3 = 10000

print(age_in_minutes(birth_year1))
print(age_in_minutes(birth_year2))
print(age_in_minutes(birth_year3))

