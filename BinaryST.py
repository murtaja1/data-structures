# Binary Search Tree
# 1. in the left subtree the value of the node is less than or equal to its parent node's value.
# 2. in the right subtree the value of the node is greater than its parent node's value.
# check visualisation\bianrysearchtree.png
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
    # time complexity is O(N) for pre, in and level order traversal.
    # space complexity is O(N) for pre, in and level order traversal.
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