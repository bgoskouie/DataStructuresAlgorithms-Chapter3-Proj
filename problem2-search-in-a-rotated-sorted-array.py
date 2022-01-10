# Search in a Rotated Sorted Array
# You are given a sorted array which is rotated at some random pivot point.

# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

# Example:

# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

# Here is some boilerplate code and test cases to start with:

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return search_recur(input_list, 0, len(input_list) - 1, number)

def search_recur(input_list, start, stop, number):
    # start, stop and mid are indices
    if input_list[start] < input_list[stop]:
        # array is sorted but number is not within it
        if number > input_list[stop] or number < input_list[start]:
            return -1
    if start == stop:
        return start
    if number == input_list[start]:
        return start
    if number == input_list[stop]:
        return stop
    # raise Exception(f"should not reach here: start={start}, stop={stop}")
    mid = (start + stop) // 2
    if input_list[mid] == number:
        return mid
    if mid == stop - 1:
        return -1
    elif input_list[mid] >= input_list[start]:
        # left segment is sorted
        if number >= input_list[start] and number <= input_list[mid]:
            return search_recur(input_list, start, mid, number)
        else:
            # right is unsorted and number is in right segment
            return search_recur(input_list, mid, stop, number)
    else:
        # right segment is sorted
        if number >= input_list[mid] and number <= input_list[stop]:
            return search_recur(input_list, mid, stop, number)
        else:
            # left is unsorted and number is in left segment
            return search_recur(input_list, start, mid, number)
    return -1


def linear_search(input_list, number):
    # this is of O(n) just for the test_function to use
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    print(linear_search(input_list, number))
    print(rotated_array_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
a = 0
