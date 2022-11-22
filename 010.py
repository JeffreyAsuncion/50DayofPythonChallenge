"""
Extra Challenge: Tuple of Student Sex
You work for a school and your boss wants to know how many 
female and male students are enrolled in the school. The school
has saved the students in a list. Your task is to write a code that 
will count how many males and females are in the list. Here is a 
list below:
students = ['Male', 'Female', 'female', 'male', 'male', 'male',
 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
Your code should return a list of tuples. The list above should 
return:
[(‘Male’,7), (‘female’,6)]
"""

def count_sex(students):
    """
    count how many males and females are in the list

    Args:
        student list[str]
    
    Return
        list[tuple]
    """
    male_count = 0
    female_count = 0 

    for i in students:
        if i.lower() == 'male':
            male_count += 1
        if i.lower() == 'female':
            female_count += 1
    
    return [('Male', male_count),('female', female_count)]



students = ['Male', 'Female', 'female', 'male', 'male', 'male',
 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

validation_value = [('Male',7), ('female',6)]

print(count_sex(students))