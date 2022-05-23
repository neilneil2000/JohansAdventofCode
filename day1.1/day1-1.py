
# Online Python - IDE, Editor, Compiler, Interpreter

import sys

b = sys.maxsize
c = 0
result = [0]


with open('day1.txt', 'r') as seed_file:
    for line in seed_file:
        if int(line) > b:
            c = c + 1
            result[0] = c
            b = int(line)
        else:
            b = int(line)


print ("number of increases is", result)
