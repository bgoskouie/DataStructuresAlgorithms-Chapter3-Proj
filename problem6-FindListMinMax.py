# Max and Min in a Unsorted Array
# In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

# Bonus Challenge: Is it possible to find the max and min in a single traversal?

# Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None, None
    smallest = ints[0]
    largest = ints[0]
    for elm in ints:  # single traversal
        if elm > largest:
            largest = elm
        if elm < smallest:
            smallest = elm
    return smallest, largest


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# edge case all numbers being the same
print ("Pass" if ((9, 9) == get_min_max(5 * [9])) else "Fail")

#edge case empty list
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")


