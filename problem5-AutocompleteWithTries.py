# Building a Trie in Python
# Before we start let us reiterate the key components of a Trie or Prefix Tree.
# A trie is a tree-like data structure that stores a dynamic set of strings.
# Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

# Before we move into the autocomplete function we need to create a working trie for storing strings.
# We will create two classes:

# A Trie class that contains the root node (empty string)
# A TrieNode class that exposes the general functionality of the Trie, like inserting
# a word or finding the node which represents a prefix.
# Give it a try by implementing the TrieNode and Trie classes below!


def s_traverse(root, prefix):
    ## Traverses in the trie, finds and returns the node that represents this prefix or a part of it
    # OUTPUTS:
    # returns true if all letters of "prefix" are found
    # then node.is_word will indicate if it represents a meaningful word
    # chrs will indicate the rest of the characters of "traverse" that are not found
    node = root
    chrs = list(prefix)
    while len(chrs) > 0:
        c = chrs[0]
        if c in node.children.keys():
            node = node.children[c]
        else:
            # Only a part of prefix is found!
            # insert the rest of the characters in the TrieNode
            return node, False, chrs
        chrs.pop(0)  # remove first element
    # whole prefix is found!
    return node, True, []

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, chrs):
        ## Add a child node in this Trie
        if len(chrs) == 0:
            return
        c = chrs[0]
        next = TrieNode()
        if len(chrs) == 1:
            next.is_word = True
        self.children.update({c: next})
        chrs.pop(0)
        # recursively call itself to insert the rest of the characters
        next.insert(chrs)

    def traverse(self, prefix):
        return s_traverse(self, prefix)

    def suffixes(self, prefix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        node, found_flag, chars = s_traverse(self, prefix=prefix)
        found_suffixes_l = list()
        # if not found_flag:
        self.find_suffix_recur(prefix, node, found_suffixes_l)
        return found_suffixes_l

    def find_suffix_recur(self, prefix, node, found_suffixes_l):
        # if len(node.children.keys()) == 0:
        #     return
        if prefix == "antholog" or prefix == "anthology":
            a = 0
        if node.is_word:
            found_suffixes_l.append(prefix)
        for child, node_child in node.children.items():
            self.find_suffix_recur(prefix + child, node_child, found_suffixes_l)
            # found_suffixes_l.append()

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node, found_flag, chrs = self.traverse(word)
        if not found_flag:
            node.insert(chrs)

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node, found_flag, chars = self.traverse(prefix)
        return node, found_flag, chars

    def traverse(self, prefix):
        return s_traverse(self.root, prefix)
        ## Traverses in the trie, finds and returns the node that represents this prefix or a part of it
        # OUTPUTS:
        # returns true if all letters of "prefix" are found
        # then node.is_word will indicate if it represents a meaningful word
        # chrs will indicate the rest of the characters of "traverse" that are not found
        # node = self.root
        # chrs = list(prefix)
        # while len(chrs) > 0:
        #     c = chrs[0]
        #     if c in node.children.keys():
        #         node = node.children[c]
        #     else:
        #         # Only a part of prefix is found!
        #         # insert the rest of the characters in the TrieNode
        #         return node, False, chrs
        #     chrs.pop(0)  # remove first element
        # # whole prefix is found!
        # return node, True, []


# Testing it all out
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

MyTrie = Trie()
MyTrie.insert("ant")

wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

node1, found1, fg1 = MyTrie.find("triggerss")
node2, found2, fg2 = MyTrie.find("trigger")
node3, found3, fg3 = MyTrie.find("trigg")
out = MyTrie.root.suffixes("ant")
print(out)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
