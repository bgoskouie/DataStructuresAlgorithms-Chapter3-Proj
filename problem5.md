Analysis for different functions:

insert:
Time Complexity:   O(n)
Space Complexity:  O(n)

find:
Time Complexity:   O(n)
Space Complexity:  O(n)

s_traverse:
Time: O(n)
Space O(n)

TrieNode :: insert:
Time O(n)
Space O(n)

TrieNode :: traverse:
same as s_traverse

TrieNode :: find_suffix_recur
Time Complexity:   O(n)
Space Complexity:  O(n)

TrieNode :: suffixes
calls one s_traverse then calls find_suffix_recur.
Time Complexity:   O(n)
Space Complexity:  O(n)


Trie :: traverse:
same as s_traverse

Trie :: find:
calls traverse, same as that

Trie :: insert:
calls traverse and then recursively calls itself
Time Complexity:   O(n)
Space Complexity:  O(n)


The algrithm uses a trie.
The alphabet size needs to be multiplied to the space complexity.
