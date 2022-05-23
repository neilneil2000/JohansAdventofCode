import sys

b = sys.maxsize
c = 0
increase = [0]
results = []
list_sum = []

# create a list

seed_file = open('day1_2.txt').read().splitlines()

def sliding_window(elements, window_size):

    if len(elements) <= window_size:
        return elements
		
    for i in range(len(elements) - window_size + 1):
        results.append(elements[i:i+window_size])
				
sliding_window(seed_file, 3)

# print(results)

for x in range (len(results)):
       list_sum.append(int(results[x][0]) + int(results[x][1]) + int(results[x][2]))
  
 
for y in list_sum:
    if y > b:
        c = c + 1
        increase[0] = c
        b = y
    else:
        b = y


print ("number of increases", increase[0])
