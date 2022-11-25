# AVL Tree: is a self-balancing binary search tree where the difference between the left and right subtrees 
# can't be more than one node for all nodes. check image: visualization\AVLTree\AVL tree.png
# why: to make the time complexity O(logN) instead of O(n) in BST.

# the four conditions:
    # 1- Left Left condition and rotation is required.
    # to know it's left, left: 
        # 1. find the unbalanced node.
        # 2. if you only moves to the left of the node, by two nodes (find the path to the grandchild, "if has two grands then take the one with greater height") then it's left, left condition.
    # whenever faced with left, left condition, do Right rotation.
    # sudo code: check visualization\AVLTree\AVL left left condition sudo code.png

    # 2- Left, Right condition and rotation is required.
    # to know it's Left, Right: 
        # 1. find the unbalanced node.
        # 2. if you only moves to the Left and then Right of the node, by two nodes (find the path to the grandchild, "if has two grands then take the one with greater height") then  it's Left Right condition.
    # whenever faced with Left, Right condition, do Left then Right rotation.
    # sudo code: check visualization\AVLTree\AVL left right condition sudo code.png and visualization\AVLTree\AVL left right condition.png

    # 3- Right Right condition and rotation is required.
    # to know it's Right, Right: 
        # 1. find the unbalanced node.
        # 2. if you only moves to the Right of the node, by two nodes (find the path to the grandchild, "if has two grands then take the one with greater height") then it's Right, Right condition.
    # whenever faced with Right, Right condition, do Left rotation.
    # sudo code: check visualization\AVLTree\AVL Right Right condition sudo code.png

    # 4- Right Left condition and rotation is required.
    # to know it's Right Left: 
        # 1. find the unbalanced node.
        # 2. if you only moves to the left and then right of the node, by two nodes (find the path to the grandchild, "if has two grands then take the one with greater height") then  it's Right, Left condition.
    # whenever faced with Right Left condition, do Right then Left rotation.
    # sudo code: check visualization\AVLTree\AVL right left condition sudo code.png and visualization\AVLTree\AVL right left condition.png

from queue import LLQueue

class AVLTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    # time complexity is O(N)
    # space complexity is O(1)
    def searchNode(self, root, value):
        current = root
        while not current:
            if value == current.data:
                return current
            elif value < current.data:
                current = current.left
            else: current = current.right
        return "Node was not found!"

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

    def levelOrderTraversal(self):
        if not self:
            return 
        else:
            queue = LLQueue()
            queue.enQueue(self)
            while not queue.isEmpty():
                current = queue.deQueue()
                print(current.data)
                if current.left:
                    queue.enQueue(current.left)
                if current.right:
                    queue.enQueue(current.right)

    # INSERTION:
    def insertNode(self, rootNode, value):
        # note: the insertion is done firstly then balancing the tree.
        if not rootNode:
            return AVLTree(value)
        elif value < rootNode.data:
            rootNode.left = self.insertNode(rootNode.left, value)
        else:
            rootNode.right = self.insertNode(rootNode.right, value)
        
        rootNode.height = 1 + max(self.getHeight(rootNode.left), self.getHeight(rootNode.right))
        balance = self.getBalance(rootNode)
        # Left, Left condition.
        if balance > 1 and value < rootNode.left.data:
            return self.rightRotation(rootNode)
        # Left, Right condition.
        if balance > 1 and value > rootNode.left.data:
            rootNode.left = self.leftRotation(rootNode.left) # to make it left, left condition firstly.
            return self.rightRotation(rootNode)
        # Right, Right condition.
        if balance < -1 and value > rootNode.right.data:
            return self.leftRotation(rootNode)
        # Right, Left condition.
        if balance < -1 and value < rootNode.right.data:
            rootNode.right = self.rightRotation(rootNode.right) # to make it right, right condition firstly.
            return self.leftRotation(rootNode)
        return rootNode

    def getHeight(self, rootNode):
        if not rootNode:
            return 0
        return rootNode.height

    def getBalance(self, rootNode):
        if not rootNode:
            return 0
        return self.getHeight(rootNode.left) - self.getHeight(rootNode.right)

    def rightRotation(self, unbalancedNode):
        newRoot = unbalancedNode.left
        unbalancedNode.left = unbalancedNode.left.right
        newRoot.right = unbalancedNode
        unbalancedNode.height = 1 + max(self.getHeight(unbalancedNode.left), self.getHeight(unbalancedNode.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        return newRoot

    def leftRotation(self, unbalancedNode):
        newRoot = unbalancedNode.right
        unbalancedNode.right = unbalancedNode.right.left
        newRoot.left = unbalancedNode
        unbalancedNode.height = 1 + max(self.getHeight(unbalancedNode.left), self.getHeight(unbalancedNode.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        return newRoot

newAVL = AVLTree(5)
newAVL = newAVL.insertNode(newAVL, 10)
newAVL = newAVL.insertNode(newAVL, 15)
newAVL = newAVL.insertNode(newAVL, 20)
newAVL.levelOrderTraversal()
