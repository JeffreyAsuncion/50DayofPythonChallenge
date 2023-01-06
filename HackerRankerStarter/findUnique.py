import math
import os
import random
import re
import sys


# a = [1,2,3,4,3,2,1]
a = [0,0,1]
map = {}

for i in range(len(a)):
    if a[i] in map:
        map[a[i]] += 1
    else:
        map[a[i]] = 1
print(map)

for k,v in map.items():
    if v == 1:
        print(k)
    # if v ==1:
    #     print(k)


