 # Trie: a tree-based data structure that organizes info in a hierarchy. check   visualization\Trie\Trie.png
 # Properties:
    # 1. it is typically used to store or search strings in space and time efficient way.
    # 2. any node in trie can store non-repetitive multiple characters.
    # 3. every node stores link of the next character of the string.
    # 4. every node keeps track of 'end of string'.

# when to use Trie:
    # - spelling checker.
    # - auto completion.

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    # check visualization\Trie\Trie Insertion.png
    # time complexity is O(n) where n is the length of the word.
    # space complexity is O(n)
    def insertNode(self, word):
        current = self.root
        for char in word:
            node = current.children.get(char)
            if not node:
                node = TrieNode()
                current.children.update({char:node}) 
            current = node
        current.endOfString = True
        return "Successfully Inserted!"

    # time complexity is O(n) where n is the length of the word.
    # space complexity is O(1)
    def searchNode(self, word): 
        current = self.root
        for char in word:
            node = current.children.get(char)
            if not node:
                return False
            current = node
        return current.endOfString

newTrie = Trie()
print(newTrie.insertNode('h'))
# print(newTrie.insertNode('hhl'))
# print(newTrie.searchNode('hell'))