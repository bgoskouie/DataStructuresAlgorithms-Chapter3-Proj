Time Complexity:  O(n * log(n))
Space Complexity:  O(n)

The algorithm first sorts the data with merge-sort method whose time complexity is n*log(n) and then runs an O(n) loop on the elements to solve the problem in the rearrange_digits function.
The overall Time complexity would be still O(n * log(n)).
The occuied space is of O(n) as it calls itself and as mergesort function calls itself it occupied more memory (i.e. O(n)).

