Time Complexity:  O(n * log(n))
Space Complexity:  O(1)

The algorithm first sorts the data with merge-sort method whose time complexity is n*log(n) and then runs an O(n) loop on the elements to solve the problem.
The overall Time complexity would be still n * log(n).
The occuied space is of O(1) as it does't change (it is constant) for different input list length (n).
