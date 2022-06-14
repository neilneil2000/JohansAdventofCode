
# Online Python - IDE, Editor, Compiler, Interpreter

horizontal_pos = 0
depth = 0

with open('day2-1.txt', 'r') as seed_file:

    for line in seed_file:
        commands = line.split()
        hor_pos, amount = commands[0], int(commands[1])
        if 'forward' in hor_pos:
            horizontal_pos += amount
        elif 'up' in hor_pos:
            depth -= amount
        elif 'down' in hor_pos:
            depth += amount	

print('the horizontal position =', horizontal_pos,'and the depth =', depth)
total = horizontal_pos * depth
print('the total =', total)