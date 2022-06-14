
horizontal_pos = 0
depth = 0
aim = 0

with open('day2-1.txt', 'r') as seed_file:

    for line in seed_file:
        commands = line.split()
        hor_pos, amount = commands[0], int(commands[1])
        if 'forward' in hor_pos:
            horizontal_pos += amount
            depth += (amount*aim)
        elif 'up' in hor_pos:
            aim -= amount
        elif 'down' in hor_pos:
            aim += amount


print('the horizontal position =', horizontal_pos,'and the depth =', depth)
total = horizontal_pos * depth
print('the total =', total)

