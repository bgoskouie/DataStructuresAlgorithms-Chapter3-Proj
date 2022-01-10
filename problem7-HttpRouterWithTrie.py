# HTTPRouter using a Trie
# For this exercise we are going to implement an HTTPRouter like you would find in a typical web server
# using the Trie data structure we learned previously.

# There are many different implementations of HTTP Routers such as regular expressions or simple
# string matching, but the Trie is an excellent and very efficient data structure for this purpose.

# The purpose of an HTTP Router is to take a URL path like "/", "/about", or
# "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return.
# In a dynamic web server, the content will often come from a block of code called a handler.

# First we need to implement a slightly different Trie than the one we used for autocomplete.
# Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

# In addition to a path though, we need to know which function will handle the http request.
# In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler
# which would be responsible for handling requests to that path. For the sake of simplicity we will just
# use a string that we can print out to ensure we got the right handler

# We could split the path into letters similar to how we did the autocomplete Trie, but this would result
# in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site.
# A more sensible way to split things would be on the parts of the path that are separated by slashes ("/").
# A Trie with a single path entry of: "/about/me" would look like:

# (root, None) -> ("about", None) -> ("me", "About Me handler")

# We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes.
# We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

# Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding
# routes and associated handlers. It should also support adding a handler by path and looking up a handler by path.
# All of these operations will be delegated to the RouteTrie.

# Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character

# Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.

# More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page.
# Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.

def s_traverse(root, segments_l):
    ## Traverses in the trie, finds and returns the node that represents this prefix or a part of it
    # OUTPUTS:
    # returns true if all pieces of segments_l are found
    # then node.is_word will indicate if it represents a meaningful word
    # chrs will indicate the rest of the characters of "traverse" that are not found
    node = root
    # chrs = list(prefix)
    while len(segments_l) > 0:
        piece = segments_l[0]
        if piece in node.children.keys():
            node = node.children[piece]
        else:
            # Only a part of prefix is found!
            # insert the rest of the characters in the RouteTrieNode
            return node, False, segments_l
        segments_l.pop(0)  # remove first element
    # whole prefix is found!
    return node, True, []

## Represents a single node in the Trie
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler_str=None):
        # Initialize the node with children as before, plus a handler
        self.is_word = False
        self.children = {}
        self.set_handler(handler_str)

    def set_handler(self, handler):
        self.handler_str = handler

    def handler(self):
        if self.handler_str is not None:
            # execute handler function
            print(self.handler_str)
            return True
        else:
            # handler is not set up
            return False

    def insert(self, segments_l, handler_str):
        # Insert the node as before
        ## Add a child node in this Trie
        if len(segments_l) == 0:
            return
        piece = segments_l[0]
        next = RouteTrieNode()
        if len(segments_l) == 1:
            next.is_word = True
            next.set_handler(handler_str)
        self.children.update({piece: next})
        segments_l.pop(0)
        # recursively call itself to insert the rest of the characters
        next.insert(segments_l, handler_str)

    def traverse(self, segments_l):
        return s_traverse(self, segments_l)

    def suffixes(self, segments_l=[]):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        node, found_flag, chars = s_traverse(self, segments_l=segments_l)
        found_suffixes_l = list()
        # if not found_flag:
        self.find_suffix_recur(segments_l, node, found_suffixes_l)
        return found_suffixes_l

    def find_suffix_recur(self, segments_l, node, found_suffixes_l):
        # if len(node.children.keys()) == 0:
        #     return
        if segments_l == "antholog" or segments_l == "anthology":
            a = 0
        if node.is_word:
            found_suffixes_l.append(segments_l)
        for child, node_child in node.children.items():
            self.find_suffix_recur(segments_l + child, node_child, found_suffixes_l)
            # found_suffixes_l.append()

## The Trie itself containing the root node and insert/find functions
class RouteTrie:
    def __init__(self, root_handler_str, not_found_handler_str=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler_str)
        self.not_found_handler_str = not_found_handler_str

    def not_found_handler(self):
        print(self.not_found_handler_str)

    def insert(self, segments_l, handler_str):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node, found_flag, remaining_segments_l = self.traverse(segments_l)
        if not found_flag:
            node.insert(remaining_segments_l, handler_str)

    def find(self, segments_l):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        ## Find the Trie node that represents this prefix
        node, found_flag, segments = self.traverse(segments_l)
        return node, found_flag, segments

    def handle(self, node, found_flag):
        if found_flag:
            if not node.handler():
                self.not_found_handler()
        else:
            self.not_found_handler()

    def find_and_handle(self, segments_l):
        node, found_flag, segments = self.find(segments_l)
        self.handle(node, found_flag)

    def traverse(self, segments_l):
        return s_traverse(self.root, segments_l)


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler_str, not_found_handler_str):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie_ = RouteTrie(root_handler_str, not_found_handler_str)

    def add_handler(self, path, handler_str):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        segments_l = self.split_path(path)
        self.routeTrie_.insert(segments_l, handler_str)
        a = 0

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        segments_l = self.split_path(path)
        self.routeTrie_.find_and_handle(segments_l)
        a = 0

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        split_l = path.split('/')
        # below index 1 returns [] if 1 is not in the range
        if len(split_l) > 0 and split_l[0] == '':
            split_l.pop(0)
        if len(split_l) > 0 and split_l[len(split_l) - 1] == '':
            split_l.pop(len(split_l) - 1)
        return split_l

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
router.lookup("/") # should print 'root handler'
router.lookup("/home") # should print 'not found handler' or None if you did not implement one
router.lookup("/home/about") # should print 'about handler'
router.lookup("/home/about/") # should print 'about handler' or None if you did not handle trailing slashes
router.lookup("/home/about/me") # should print 'not found handler' or None if you did not implement one

