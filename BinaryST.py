# Binary Search Tree
# 1. in the left subtree the value of the node is less than or equal to its parent node's value.
# 2. in the right subtree the value of the node is greater than its parent node's value.
# check visualization\bianrysearchtree.png
#  
from queue import LLQueue

class BinaryST:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    # time complexity is O(logN), because it's calling the func by half (drops half the nodes) each time.
    # space complexity is O(logN), because it's saving the func by half each time in the stack.
    def insertBTNode(self, root, value):
        if root.data == None:
            root.data = value
        elif value <= root.data:
            if not root.left:
                root.left = BinaryST(value)
            else: self.insertBTNode(root.left, value)
        else:
            if not root.right:
                root.right = BinaryST(value)
            else:
                self.insertBTNode(root.right, value)

    def _minValue(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    # time complexity is O(logN)
    # space complexity is O(logN)
    def deleteNode(self, root, value):
        if not root:
            return root
        if value < root.data:
            root.left = self.deleteNode(root.left, value)
        elif value > root.data:
            root.right = self.deleteNode(root.right, value)
        else:
            # if has one child or leaf
            if not root.left:
                temp = root.right # might has value or None.
                root = None
                return temp
            if not root.right:
                temp = root.left
                root = None
                return temp
                   
            # if has two children.
            successor = self._minValue(root.right) # get the mini left (successor) in the right subtree
            root.data = successor.data 
            root.right = self.deleteNode(root.right, successor.data) # remove the min value that was taken in place of the deleted.
        return root
    # time complexity is O(logN)
    # space complexity is O(logN)
    def searchNode(self, root, value): # can be done in an iterative way, check AVL Tree.
        if not root or root.data == value:
            return root
        if value < root.data: self.searchNode(root.left, value)
        else: self.searchNode(root.right, value)
    # time complexity is O(1)
    # space complexity is O(1)
    def deleteBST(self):
        self.data = None
        self.right = None
        self.left = None
    # time complexity is O(N) for pre, in, post and level order traversal.
    # space complexity is O(N) for pre, in, post and level order traversal.
    def preOrderTraversal(self, rootNode):
        if not rootNode:
            return 
        print(rootNode.data)
        self.preOrderTraversal(rootNode.left)
        self.preOrderTraversal(rootNode.right)

    def inOrderTraversal(self, rootNode):
        if not rootNode:
            return 
        self.inOrderTraversal(rootNode.left)
        print(rootNode.data)
        self.inOrderTraversal(rootNode.right)

    def postOrderTraversal(self, rootNode):
        if not rootNode:
            return 
        self.postOrderTraversal(rootNode.left)
        self.postOrderTraversal(rootNode.right)
        print(rootNode.data)

    def levelOrderTraversal(self, rootNode):
        if not rootNode:
            return 
        else:
            queue = LLQueue()
            queue.enQueue(rootNode)
            while not queue.isEmpty():
                current = queue.deQueue()
                print(current.data)
                if current.left:
                    queue.enQueue(current.left)
                if current.right:
                    queue.enQueue(current.right)


root = BinaryST(None)
root.insertBTNode(root, 10)
root.insertBTNode(root, 20)
root.insertBTNode(root, 5)
root.insertBTNode(root, 33)
root.insertBTNode(root, 22)
root.insertBTNode(root, 55)
root.insertBTNode(root, 11)
root.insertBTNode(root, 99)
root.deleteNode(root, 11)
root.levelOrderTraversal(root)
