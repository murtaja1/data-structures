# Binary Heap:
    # check visualization\BinaryHeap\time space of binary heap.png
    # . types of binary heap: check visualization\BinaryHeap\types of binary heap.png
        # 1. Min Heap: the value of each node is less than or equal to value of both its children.
        # 2. Max Heap: the opposite of Min heap the value of each node is greater than or equal to value of both its children.
    # it's a complete tree(all levels are completely filled except possibly the last level and the last level has all keys as left as possible). This
    # property of binary heap makes them suitable to be stored in an array.
    
#  Why use binary heap:
    # - to find minimum or maximum number among a set of numbers in logN time. 
    #   And also we can m  ake sure that inserting additional numbers does not take more than logN time. 
# Practical Use:
    # 1. Prim's Algorithm.
    # 2. Heap Sort.
    # 3. Priority Queue.

class BinaryHeap:
    # time complexity is O(1 )
    # space complexity is O(N)
    def __init__(self, size) -> None:
        self.binaryHeap = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

    # time complexity is O(1)
    # space complexity is O(1)
    def peek(self, root):
        if not root:
            return 
        return root.binaryHeap[1]

    # time complexity is O(1)
    # space complexity is O(1)
    def size(self, root):
        if not root:
            return 
        return root.heapSize

    # INSERTION.
    # time complexity is O(logN)
    # space complexity is O(logN)
    def heapifyInsertion(self, valueIndex, heapType):  
        parentIndex = int(valueIndex/2)
        if valueIndex <= 1:
            return
        if heapType == 'Min':
            if self.binaryHeap[valueIndex] < self.binaryHeap[parentIndex]:
                temp = self.binaryHeap[valueIndex]
                self.binaryHeap[valueIndex] = self.binaryHeap[parentIndex]
                self.binaryHeap[parentIndex] = temp
            self.heapifyInsertion(parentIndex, heapType)
        elif heapType == "Max":
            if self.binaryHeap[valueIndex] > self.binaryHeap[parentIndex]:
                temp = self.binaryHeap[valueIndex]
                self.binaryHeap[valueIndex] = self.binaryHeap[parentIndex]
                self.binaryHeap[parentIndex] = temp
            self.heapifyInsertion(parentIndex, heapType)

    # time complexity is O(logN)
    # space complexity is O(logN)
    def insertNode(self, value, heapType):
        if self.maxSize == self.heapSize + 1:
            return 'Binary Heap is full!'
        self.binaryHeap[self.heapSize + 1] = value
        self.heapSize += 1
        self.heapifyInsertion(self.heapSize, heapType)
        return 'Node was inserted successfully!'

    # EXTRACTION.
    # time complexity is O(logN)
    # space complexity is O(logN)
    def heapifyExtraction(self, index, heapType):
        leftIndex = index * 2
        rightIndex = index * 2 + 1
        swapChildIndex = 0
        if self.heapSize < leftIndex:
            return
        # if one child.
        elif leftIndex == self.heapSize:
            if heapType == 'Min':
                if self.binaryHeap[index] > self.binaryHeap[leftIndex]:
                    temp = self.binaryHeap[index]
                    self.binaryHeap[index] = self.binaryHeap[leftIndex]
                    self.binaryHeap[leftIndex] = temp
                return
            else: 
                if self.binaryHeap[index] < self.binaryHeap[leftIndex]:
                    temp = self.binaryHeap[index]
                    self.binaryHeap[index] = self.binaryHeap[leftIndex]
                    self.binaryHeap[leftIndex] = temp
                return
        # if has two children.
        else:
            if heapType == 'Min':
                # Min then find the smallest child then swap with parent
                if self.binaryHeap[leftIndex] < self.binaryHeap[rightIndex]:
                    swapChildIndex = leftIndex
                else:
                    swapChildIndex = rightIndex

                if self.binaryHeap[index] > self.binaryHeap[swapChildIndex]:
                    temp = self.binaryHeap[index]
                    self.binaryHeap[index] = self.binaryHeap[swapChildIndex]
                    self.binaryHeap[swapChildIndex] = temp
            else:
                # Max then find the largest child then swap with parent
                if self.binaryHeap[leftIndex] > self.binaryHeap[rightIndex]:
                    swapChildIndex = leftIndex
                else:
                    swapChildIndex = rightIndex
                if self.binaryHeap[index] < self.binaryHeap[swapChildIndex]:
                    temp = self.binaryHeap[index]
                    self.binaryHeap[index] = self.binaryHeap[swapChildIndex]
                    self.binaryHeap[swapChildIndex] = temp
        self.heapifyExtraction(swapChildIndex, heapType)

    # time complexity is O(1)
    # space complexity is O(1)
    def deleteBP(self): 
        self.binaryHeap = None
        self.heapSize = 0
        self.maxSize = 0 

    # time complexity is O(logN)
    # space complexity is O(logN)
    def extractNode(self, heapType):
        if self.heapSize == 0:
            return
        extracted = self.binaryHeap[1]
        self.binaryHeap[1] = self.binaryHeap[self.heapSize]
        self.binaryHeap[self.heapSize] = None
        self.heapSize -= 1
        self.heapifyExtraction(1, heapType)
        return extracted
            
    # time complexity is O(N) for pre, in, post and level order traversal.
    # space complexity is O(N) for pre, in, post and level order traversal.
    # root => left => right
    def preOrderTraversal(self, index = 1):
        if index >= self.heapSize + 1:
            return 
        print(self.binaryHeap[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index * 2 + 1)

    # left => root => right
    def inOrderTraversal(self, index = 1):
        if  index >= self.heapSize + 1:
            return 
        self.inOrderTraversal(index * 2)
        print(self.binaryHeap[index])
        self.inOrderTraversal(index * 2 + 1)

    # left => right => root
    def postOrderTraversal(self, index = 1):
        if  index >= self.heapSize + 1:
            return 
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.binaryHeap[index]) 

    # level by level
    def leverOrderTraversal(self, index = 1):
        if not self.binaryHeap[index]:
            return 
        for i in range(1, self.heapSize   + 1):
            print(self.binaryHeap[i])

binaryHeap = BinaryHeap(5)

binaryHeap.insertNode(4, 'Min')
binaryHeap.insertNode(5, 'Min')
binaryHeap.insertNode(2, 'Min')
binaryHeap.insertNode(1, 'Min')
print('deleted', binaryHeap.extractNode('Min'))

binaryHeap.leverOrderTraversal()


