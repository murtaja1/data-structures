# class TreeNode:
#   def __init__(self, data, children = []) -> None:
#     self.data = data
#     self.children = children

#   def __str__(self, level=0):
#       ret = "  " * level + str(self.data)  + "\n"
#       for child in self.children:
#           ret += child.__str__(level + 1)
#       return ret
  
#   def addChild(self, treeNode):
#     self.children.append(treeNode)

# tree = TreeNode('Drinks', [])
# cold = TreeNode('Juice', [])
# hot = TreeNode('Hot', [])

# orange = TreeNode('orange', [])
# lemon = TreeNode('lemon', [])
          
# coffee = TreeNode('coffee', [])
# tea = TreeNode('Tea', [])

# tree.addChild(cold)
# tree.addChild(hot)

# cold.addChild(orange)
# cold.addChild(lemon)

# hot.addChild(coffee)
# hot.addChild(tea)
# print(tree)

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

tree = TreeNode('Drinks')

tree.left = TreeNode('Juice')
tree.right = TreeNode('Hot')

tree.left.left = TreeNode('orange')
tree.left.right = TreeNode('lemon')
          
tree.right.left = TreeNode('coffee')
tree.right.right = TreeNode('Tea')

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

# insertNewNode(tree, 'iam new node')
