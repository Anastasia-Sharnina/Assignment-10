# main.py

from module1 import find_two_smallest
from module2 import list1, list2, list3, list4

lists = [list1, list2, list3, list4]

with open('result.txt', 'w') as file:
    for i, lst in enumerate(lists):
        try:
            smallest_values = find_two_smallest(lst)
            file.write(f"List {i + 1}: Smallest values are {smallest_values}\n")
        except ValueError as e:
            file.write(f"List {i + 1}: Error - {str(e)}\n")
