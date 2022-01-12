Insert:
Time Complexity:   O(n)
Space Complexity:   O(n)

Find:
Time Complexity:   O(n)
Space Complexity:   O(n)

Static methods:
s_traverse:
Time: O(n)
Space O(n)

RouteTrieNode class:

RouteTrieNode :: set_handler
Time: O(1)
Space O(1)

RouteTrieNode :: handler
Time: O(1)
Space O(1)

RouteTrieNode :: insert:
Time O(n)
Space O(n)

RouteTrieNode :: traverse:
same as s_traverse

RouteTrieNode :: find_suffix_recur
Time Complexity:   O(n)
Space Complexity:  O(n)

RouteTrieNode :: suffixes
calls one s_traverse then calls find_suffix_recur.
Time Complexity:   O(n)
Space Complexity:  O(n)


RouteTrie class:
RouteTrie :: not_found_handler
Time: O(1)
Space O(1)

RouteTrie :: handle
calls not_found_handler
Time: O(1)
Space O(1)

RouteTrie :: traverse:
same as s_traverse
Time Complexity:   O(n)
Space Complexity:  O(n)

RouteTrie :: find:
calls traverse, same as that
Time Complexity:   O(n)
Space Complexity:  O(n)

RouteTrie :: insert:
calls traverse and then recursively calls itself
Time Complexity:   O(n)
Space Complexity:  O(n)

RouteTrie :: find_and_handle
calls not_found_handler then find
Time Complexity:   O(n)
Space Complexity:  O(n)


The algorithm uses a trie data structure and thus space and time are of Big O of (n).
It implements a RouteTrieNode object that holds every instance of an object held within a trie.
It also implements a RouteTie object that holds the whole trie. The whole trie includes RouteTrieNode objects.
It also implements a Router object that holds the trie and implements the wrapping functinons, creating the trie, inserting, adding handler,...
