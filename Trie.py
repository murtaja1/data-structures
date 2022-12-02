 # Trie: a tree-based data structure that organizes info in a hierarchy. check   visualization\Trie\Trie.png
 # Properties:
    # 1. it is typically used to store or search strings in space and time efficient way.
    # 2. any node in trie can store non-repetitive multiple characters.
    # 3. every node stores link of the next character of the string.
    # 4. every node keeps track of 'end of string'.

# why use Trie:
    # -spelling checker.
    # -auto completion.

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

newTrie = Trie()