from queue import LLQueue

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self, level = 0):
        ret = "  " * level + str(self.data) + '\n'
        if self.left:
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret


# preOrder traversal:
def preOrderTraversal(rootNode):
    if not rootNode:
        return 
  
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)

# preOrderTraversal(tree)
def inOrderTraversal(rootNode): 
    if not rootNode:
        return 
    inOrderTraversal(rootNode.left)
    print(rootNode.data)
    inOrderTraversal(rootNode.right)

# inOrderTraversal(tree)
def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data)

# postOrderTraversal(tree)
def levelOrderTraversal(rootNode):
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
# levelOrderTraversal(tree)

# searching Binary Tree
def searchBT(rootNode, nodeValue):
    if not rootNode:
        return 
    else: 
        queue = LLQueue()
        queue.enQueue(rootNode)
        while not queue.isEmpty():
            current = queue.deQueue()
            if current.data == nodeValue:
                return 'Success!'
            if current.left:
                queue.enQueue(current.left)
            if current.right: 
                queue.enQueue(current.right)
            
        return 'Node Not Found!'

# insertion a newNode to the binary tree
def insertNewNode(rootNode, nodeValue):
    newNode = TreeNode(nodeValue)
    if not rootNode:
        rootNode = newNode
        return
    else: 
        queue = LLQueue()
        queue.enQueue(rootNode)
        while not queue.isEmpty():
            current = queue.deQueue()
            if current.left:
                queue.enQueue(current.left)
            else:
                current.left = newNode
                return 

            if current.right:
                queue.enQueue(current.right)
            else:
                current.right = newNode
                return 

tree = TreeNode('Drinks')

insertNewNode(tree, 'Juice')
insertNewNode(tree, 'Hot')
insertNewNode(tree, 'orange')
insertNewNode(tree, 'lemon')
insertNewNode(tree, 'coffee')
insertNewNode(tree, 'Tea')
levelOrderTraversal(tree)
# delete tree node.

# find and remove the deepest node.
def findDeepestNode(rootNode):
    if not rootNode:
        return 'the tree does not exits!'

    else: 
        queue = LLQueue()
        queue.enQueue(rootNode)
        while not queue.isEmpty():
            current = queue.deQueue()

            if current.left:
                queue.enQueue(current.left)

            if current.right:
                queue.enQueue(current.right)
        return current.data

def removeDeepestNode(rootNode, dNode):
    if not rootNode:
        return 'the tree does not exits!'

    else: 
        queue = LLQueue()
        queue.enQueue(rootNode)
        while not queue.isEmpty():
            current = queue.deQueue()

            if current.left:
                if current.left.data == dNode:
                    current.left.data = None
                    current.left = None
                    return 'removed'
                else:
                    queue.enQueue(current.left)

            if current.right:
                if current.right.data == dNode:
                    current.right.data = None
                    current.right = None
                    return 'removed'
                else:
                    queue.enQueue(current.right)
        return 'was not removed'

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return 'There is no tree!'
    else:
        queue = LLQueue()
        queue.enQueue(rootNode)
        while not queue.isEmpty():
            current = queue.deQueue()
            if current.data == nodeValue:
                deepestNode = findDeepestNode(tree)
                removeDeepestNode(tree, deepestNode)
                current.data = deepestNode
                return 'Node was deleted!'

            if current.left:
                queue.enQueue(current.left)

            if current.right:
                queue.enQueue(current.right)

        return 'Tree Node was not found!'
# deleteNode(tree, 'Drinks')

# delete entire node.
def deleteBT(rootNode):
    if not rootNode:
        return 'There is no tree!'
    else:
        rootNode.left = None
        rootNode.right = None
        rootNode.data= None

# deleteBT(tree)
