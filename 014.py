"""
Extra Challenge: Dictionary of names
You are given a list of names, and you are asked to write a code 
that returns all the names that start with ‘S’. Your code should 
return a dictionary of all the names that start with S and how 
many times they appear in the dictionary. Here is a list below:
names = ["Joseph","Nathan", "Sasha", "Kelly",
 "Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]
Your code should return: {“Sasha”: 1, “Sera”: 2}
"""


def dict_of_names(names):
    map = {}

    for i in names:
        if i[0].lower() == 's':
            if i in map.keys():
                map[i] += 1
            else:
                map[i] = 1

    return map

names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

print(dict_of_names(names))