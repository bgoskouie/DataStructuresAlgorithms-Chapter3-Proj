# Rearrange Array Elements
# Rearrange Array Elements so as to form two number such that their sum is maximum.
# Return these two numbers. You can assume that all array elements are in the range [0, 9].
# The number of digits in both the numbers cannot differ by more than 1.
# You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

# for e.g. [1, 2, 3, 4, 5]

# The expected answer would be [531, 42]. Another expected answer can be [542, 31].
# In scenarios such as these when there are more than one possible answers, return any one.

# Here is some boilerplate code and test cases to start with:

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # First: Sort all the elements ascending in the "input_list" items with O(n log(n))
    sorted_list = mergesort(input_list)

    # Run a for loop over all elements to create the two numbers with O(n)
    # if sorted elements are [e0 e1 e2 e3 e4 ...] in ascending order then
    # the two numbers would be:
    # num1 = ...e4e2e0   and    num2 = ...e5e3e1
    num1 = 0
    num2 = 0
    ind1 = 0
    ind2 = 0
    ind = 0
    for e in sorted_list:
        if ind % 2 == 0:
            num1 += e * (10 ** ind1)
            ind1 += 1
        else:
            num2 += e * (10 ** ind2)
            ind2 += 1
        ind += 1
    return [num1, num2]


def mergesort(items):
    """sorts elements of list "items" in place
    Time Complexity:  n * log(n)"""
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


def merge(left, right):
    """Given two sorted arrays "left" and "right" return the sorted merged array"""
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    merged += left[left_index:]
    merged += right[right_index:]
    return merged

def swap(v, i, j):
    """given an array "v" and two indices of i and j
    swaps the values and returns the same array"""
    tmp = v[j]
    v[j] = v[i]
    v[i] = tmp

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

arr = [4, 6, 2, 5, 9, 8]
sorted_list = mergesort(arr)
print(sorted_list)

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

#edge case empty list:
test_case = [[], []]
test_function(test_case)
#edge case largest numbers equal:
test_case = [[4, 6, 2, 5, 9, 9], [964, 952]]
test_function(test_case)
