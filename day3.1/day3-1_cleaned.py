
count_items = 0
y = 0
x = 0
w = [] 

with open('day3-1.txt', 'r') as seed_file:
    
    for line in seed_file:
       count_items += 1
       x = len(line.strip())
       create_list = x
       if len(w) < 1:
            w = list(line.strip())
       else:
           while x > 0:
               x -= 1
               y = int(w[x])
               w[x] = y + int(line[x])
               
print(w, count_items)

z = create_list
gamma_rate = []
epsilon_rate = []


if len(gamma_rate) < 1:
    while create_list > 0:
       create_list -= 1
       gamma_rate.append(0)
       epsilon_rate.append(0)

while z > 0:
   z -= 1
   if w[z] > count_items/2:
       gamma_rate[z] = 1
   else:
       epsilon_rate[z] = 1
	
print(gamma_rate)
print(epsilon_rate)
	
gamma = int(''.join(str(x) for x in gamma_rate), base=2)
epsilon = int(''.join(str(x) for x in epsilon_rate), base=2)		

power = gamma * epsilon

print("power consumption = ", power)      






        