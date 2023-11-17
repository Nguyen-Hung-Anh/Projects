'''
List_manipulation.py -- Nguyen Hung Anh -- 10/13/2023

# This module defines list manipulation functions:
#   - count_occurrences(l_items, key): Returns occurrences of 'key' in 'l_items'.
#   - mode(lst): Returns most frequently occurring value in 'lst'.
#   - remove_duplicates(lst): Returns a new list with duplicates removed from 'lst'.
#   - count_distinct(lst): Returns the count of distinct values in 'lst'.
# Test functions using provided examples; consider reuse opportunities.
'''

def count_occurrences(l_items, key):
    count = l_items.count(key)
    return count
def mode(l_items2):
    dict_list = {}

    for element in l_items2:
        if element in dict_list:
            dict_list[element] += 1
        else:
            dict_list[element] = 1
    max_count = max(dict_list.values())

    new_list = []
    for element in dict_list:
        count = dict_list[element]
        if count == max_count:
            new_list.append(element)
    return new_list[0]
def remove_duplicates(l_items):
    result = []

    for element in l_items:
        if element not in result:
            result.append(element)
    return result
def count_distinct(l_items2):
    distinct_set = set(l_items2)
    return len(distinct_set)
def main():
    l_items =[1,3,5,5,1,3]
    key = 3
    output_1 = count_occurrences(l_items, key)
    print("How many times the element of key appers in l_tems:", output_1)

    l_items2 = ["dog", "cat", "bird", "wumps", "cat", "wumps"]
    output_2 = mode(l_items2)
    print("Which value from the l_items2 occurs most often:", output_2)

    output_3 = remove_duplicates(l_items)
    print("A new lst with duplicates removed:", output_3)

    output_4 = count_distinct(l_items2)
    print("How many differenct values in the l_items2:", output_4)
    

if __name__ == "__main__":
    main()
