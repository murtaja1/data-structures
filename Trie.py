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

    # time complexity is O(n) where n is the length of the word.
    # space complexity is O(n)
    def deleteNode(self, root, word, index=0):
        child = word[index]
        currentNode = root.children.get(child)
        canThisNodeBeDeleted = False
        print(child, currentNode.children)
        # case 1: some other's prefix of string is same as the one that we want to delete. ex: (API, APPLE). check visualization\Trie\deletion case 1.png
        if len(currentNode.children) > 1:
            print('case 1', child)
            self.deleteNode(currentNode, word, index+1) # update the index to go to the next char.
            return False # this can't be deleted.
        # case 2: the string is a prefix of another string. ex: (API, APIS) check visualization\Trie\deletion case 2.png
        if index == len(word)-1:
            print('case 2', child)
            if len(currentNode.children) >= 1: # if it has children more than 1.
                currentNode.endOfString = False
                return False
            else:
                print('case 2 last:', child)
                root.children.pop(child)
                return True
        # case 3: other string is a prefix of this string. ex: (APIS, AP) check visualization\Trie\deletion case 3.png
        if currentNode.endOfString == True:
            print('case 3', child)
            self.deleteNode(currentNode, word, index+1)
            return False
        print('aaaaaaaaaaaa')
        # case 4: not any node depends on this string. check visualization\Trie\deletion case 4.png
        canThisNodeBeDeleted = self.deleteNode(currentNode, word, index+1)
        print('case 4', child, canThisNodeBeDeleted)
        if canThisNodeBeDeleted:
            root.children.pop(child)
            return True
        else:
            return False

newTrie = Trie()
print(newTrie.insertNode('API'))
print(newTrie.insertNode('APPLE'))
newTrie.deleteNode(newTrie.root, 'API')
print(newTrie.searchNode('API'))