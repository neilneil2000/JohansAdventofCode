
import copy

def fetch_values():
   num_entries = 0
   value_list = []
   with open('day3-1.txt', 'r') as values:
       for line in values:
           value_list.append(line.strip())
           lenght_item = len(line)
           num_entries += 1
   print("number of bits", lenght_item)
   print("total number of entries",  num_entries)
   return value_list, lenght_item, num_entries

def totgen(bit_pos, clean_value_list):
    count_entry = 0
    total_ones = 0
    y = 0
    for item in clean_value_list:
        x = int(item[bit_pos])
        total_ones = x + y 
        y = total_ones
        count_entry += 1
    print(total_ones, count_entry)
    return total_ones, count_entry

def clean_list(bit_pos, count_entry, total_ones, clean_value_list):
    temp_list = []
    temp_list.clear()
    if total_ones >= count_entry/2:
        for line in clean_value_list: 
           x = int(line[bit_pos])
           if x == 1:
               temp_list.append(line)
    else:
        for line in clean_value_list:
            x = int(line[bit_pos])
            if x == 0:
               temp_list.append(line)
    clean_value_list.clear()
    clean_value_list = temp_list.copy()
    return clean_value_list

def clean_list_co2(bit_pos, count_entry, total_ones, clean_value_list):
    temp_list = []
    temp_list.clear()
    if total_ones < count_entry/2:
        for line in clean_value_list: 
           x = int(line[bit_pos])
           if x == 1:
               temp_list.append(line)
    else:
        for line in clean_value_list:
            x = int(line[bit_pos])
            if x == 0:
               temp_list.append(line)
    clean_value_list.clear()
    clean_value_list = temp_list.copy()
    return clean_value_list

def main():
    value_list, lenght_item, num_entries = fetch_values()
    clean_value_list = value_list.copy()
    bit_pos = 0
    count_entry = 0
    total_ones = 0
    while bit_pos < lenght_item:
        print("bit position", bit_pos)
        total_ones, count_entry = totgen(bit_pos, clean_value_list)
        if count_entry == 1:
            print("reached one entry")
            break
        else:
            clean_value_list = clean_list(bit_pos, count_entry, total_ones, clean_value_list)
            bit_pos += 1
    
    oxy_value = clean_value_list.copy()        
    print("current bit pos", bit_pos, oxy_value) 
    print("determine co2")
    clean_value_list.clear
    clean_value_list = value_list.copy()
    bit_pos = 0
    while bit_pos < lenght_item:
        print("bit position", bit_pos)
        total_ones, count_entry = totgen(bit_pos, clean_value_list)
        if count_entry == 1:
            print("reached one entry")
            break
        else:
            clean_value_list = clean_list_co2(bit_pos, count_entry, total_ones, clean_value_list)
            bit_pos += 1
            
    CO2_value = clean_value_list.copy()
    print(CO2_value)
 
    life_support = int(CO2_value[0], 2) * int(oxy_value[0], 2)
    print(life_support)





if __name__ == "__main__" : main()







