class TreeNode:
  def __init__(self, data, children = []) -> None:
    self.data = data
    self.children = children

  def __str__(self, level=0):
      ret = "  " * level + str(self.data)  + "\n"
      for child in self.children:
          ret += child.__str__(level + 1)
      return ret
  
  def addChild(self, treeNode):
    self.children.append(treeNode)

tree = TreeNode('Drinks', [])
cold = TreeNode('Juice', [])
hot = TreeNode('Hot', [])

orange = TreeNode('orange', [])
lemon = TreeNode('lemon', [])

coffee = TreeNode('coffee', [])
tea = TreeNode('Tea', [])

tree.addChild(cold)
tree.addChild(hot)

cold.addChild(orange)
cold.addChild(lemon)

hot.addChild(coffee)
hot.addChild(tea)
print(tree)



