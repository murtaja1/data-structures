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

# NOTE: the x is the index of the parent cell.
# to find left child use left = cell[2x]. 
# to find right child use right = cell[2x + 1]. 

class LTree:
    def __init__(self, size) -> None:
        self.treeList = [None] * size
        self.lastUsedIndex = 0
        self.size = size
    
    def insertNode(self, nodeValue):
        if self.lastUsedIndex == self.size:
            return 'Tree is full!'
        self.lastUsedIndex += 1
        self.treeList[self.lastUsedIndex] = nodeValue

    def searchNode(self, nodeValue):
        return self.treeList.index(nodeValue)
    # root => left => right
    def preOrderTraversal(self, index = 1):
        if self.lastUsedIndex == 0:
            return 'The Tree is empty!'
        if index > self.lastUsedIndex:
            return 
        print(self.treeList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index * 2 + 1)
    # left => root => right
    def inOrderTraversal(self, index = 1):
        if self.lastUsedIndex == 0:
            return 'The Tree is empty!'
        if index > self.lastUsedIndex:
            return 
        self.inOrderTraversal(index * 2)
        print(self.treeList[index])
        self.inOrderTraversal(index * 2 + 1)
    # left => right => root
    def postOrderTraversal(self, index = 1):
        if self.lastUsedIndex == 0:
            return 'The Tree is empty!'
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.treeList[index]) 
    # level by level
    def leverOrderTraversal(self, index = 1):
        if self.lastUsedIndex == 0:
            return 'The Tree is empty!'
        if index > self.lastUsedIndex:
            return
        for i in range(1, self.lastUsedIndex + 1):
            print(self.treeList[i])

    def deleteNode(self, nodeValue):
        if self.lastUsedIndex == 0:
            return 'The Tree is empty!'
        nodeIndex = self.treeList.index(nodeValue)
        self.treeList[nodeIndex] = self.treeList[self.lastUsedIndex]
        self.treeList[self.lastUsedIndex] = None
        self.lastUsedIndex -= 1

    def deleteBT(self):
        self.treeList = None

lTree = LTree(8)
lTree.insertNode(1)
lTree.insertNode(2)
lTree.insertNode(3)
lTree.insertNode(4)
lTree.insertNode(5)

# print(lTree.searchNode(5))
# lTree.preOrderTraversal()
# lTree.leverOrderTraversal()
# print('####################')
# lTree.deleteBT()
# lTree.leverOrderTraversal() 