# module1.py

def find_two_smallest(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements.")
    
    smallest = float('inf')
    second_smallest = float('inf')
    
    for number in lst:
        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif smallest < number < second_smallest:
            second_smallest = number
    
    return smallest, second_smallest
