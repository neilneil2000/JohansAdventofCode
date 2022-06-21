"""this is Johan's part 2 of Day 3 Advent of Code 2021"""

from typing import List, Tuple


def fetch_values() -> Tuple[List[str], int]:
    """Returns values from input file"""
    value_list = []
    with open("day3.2/day3-1.txt", "r", encoding="utf-8") as values:
        for line in values:
            value_list.append(line.strip())
            lenght_item = len(line)
    return value_list, lenght_item


def totgen(bit_pos: int, clean_value_list: List[str]):
    count_entry = 0
    total_ones = 0
    y = 0
    for item in clean_value_list:
        x = int(item[bit_pos])
        total_ones = x + y
        y = total_ones
        count_entry += 1
    return total_ones, count_entry


def clean_list(
    bit_pos: int, count_entry: int, total_ones: int, clean_value_list: List[str]
) -> List[str]:
    """Remove un needed items from list"""
    temp_list = []
    temp_list.clear()
    if total_ones >= count_entry / 2:
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
    if total_ones < count_entry / 2:
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
    value_list, lenght_item = fetch_values()
    clean_value_list = value_list.copy()
    bit_pos = 0
    count_entry = 0
    total_ones = 0
    while bit_pos < lenght_item:
        total_ones, count_entry = totgen(bit_pos, clean_value_list)
        if count_entry == 1:
            print("reached one entry")
            break
        else:
            clean_value_list = clean_list(
                bit_pos, count_entry, total_ones, clean_value_list
            )
            bit_pos += 1
    oxy_value = clean_value_list.copy()

    clean_value_list.clear()  # Is this needed? Seemed to work without
    clean_value_list = value_list.copy()
    bit_pos = 0
    while bit_pos < lenght_item:
        total_ones, count_entry = totgen(bit_pos, clean_value_list)
        if count_entry == 1:
            print("reached one entry")
            break
        else:
            clean_value_list = clean_list_co2(
                bit_pos, count_entry, total_ones, clean_value_list
            )
            bit_pos += 1

    CO2_value = clean_value_list.copy()

    life_support = int(CO2_value[0], 2) * int(oxy_value[0], 2)
    print(life_support)


if __name__ == "__main__":
    main()
