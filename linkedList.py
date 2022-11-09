class Node:
  def __init__(self, value=None) -> None:
    self.value = value
    self.next = None
  
class SLinkedList:
  def __init__(self) -> None:
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next

  def __str__(self):  # -------------> the __str__ function will make our object printable.
      return str([node.value for node in self])

  def insertNode(self, value, location):
    newNode = Node(value)
    # if no nodes.
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      # if insert in the beginning.
      if location == 0:
        newNode.next = self.head
        self.head = newNode
      # if insert in the last.
      elif location == -1:
        newNode.next = None
        self.tail.next = newNode
        self.tail = newNode
        
      # if insert at a specific point.
      else:
        currentNode = self.head
        for _ in range(1, location):
          currentNode = currentNode.next

        newNode.next = currentNode.next
        currentNode.next = newNode
    
  def findNode(self, value):
    if not self.head:
      return 'Linked List does not exist!'
    for index, node in enumerate(self):
      if node.value == value:
        return node
    return 'Value is not available in the Linked List!'

  def deleteNodeByValue(self, value):
    if not self.head:
      return 'Linked List does not exist!'

    # if first node and only one node in the linked list.
    if not self.head.next:
      deletedNode = self.head
      self.head = None
      self.tail = None
      return deletedNode

    # if first node and there are more than one node in linked list! 
    elif self.head.value == value:
      deletedNode = self.head
      self.head = self.head.next
      return deletedNode

    # if last node.
    elif self.tail.value == value:
      deletedNode = self.tail
      prvNode = self.head
      for _, node in enumerate(self):
        if node.value == value:
           prvNode.next = None
           self.tail = prvNode
           return deletedNode
        prvNode = node

    # if node in the middle.
    else:
      prvNode = self.head
      for _, node in enumerate(self):
        if node.value == value: 
          deletedNode = node
          prvNode.next = deletedNode.next
          return deletedNode
        prvNode = node
    return 'Value is not available in the Linked List!'

  def removeByIndex(self, index): # ---------------> O(Index), O(N)
    if index == 0:
        self.head = self.head.next
        return
    previous_node_index = index - 1
    for c_index, node in enumerate(self):
        if c_index == previous_node_index:
            node.next = node.next.next
            if not node.next:
                self.tail = node
            return
  def clear(self):
    self.head = None
    self.tail = None
    return 

# sLinkedList = SLinkedList()
# sLinkedList.insertNode(1,0)
# sLinkedList.insertNode(2,-1)
# sLinkedList.insertNode(3,1)
# sLinkedList.insertNode(40,2)
# print('before: ', sLinkedList)
# print("clear: ",sLinkedList.clear())
# print('after: ',sLinkedList)


# Circular Linked List.
class CSLinkedList:
  def __init__(self) -> None:
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next
      # if next of the last node is the head then break.
      if node == self.head:
        break

  def __str__(self):  # -------------> the __str__ function will make our object printable.
      return str([node.value for node in self])

  def insertNode(self, value, location):
    newNode = Node(value)
    # if no nodes.
    if self.head is None:
      self.head = newNode
      self.head.next = self.head
      self.tail = newNode

    else:
      # if insert in the beginning.
      if location == 0:
        newNode.next = self.head
        self.head = newNode
        self.tail.next = self.head
      # if insert in the last.
      elif location == -1:
        newNode.next = self.head
        self.tail.next = newNode
        self.tail = newNode        
      # if insert at a specific point.
      else:
        currentNode = self.head
        for _ in range(1, location):
          currentNode = currentNode.next

        newNode.next = currentNode.next
        currentNode.next = newNode
    
  def findNode(self, value):
    if not self.head:
      return 'Linked List does not exist!'
    for _, node in enumerate(self):
      if node.value == value:
        return node
    return 'Value is not available in the Linked List!'

  def deleteNodeByValue(self, value):
    if not self.head:
      return 'Linked List does not exist!'

    # if first node and only one node in the linked list.
    if self.head == self.tail:
      deletedNode = self.head
      self.head.next = None
      self.head = None
      self.tail = None
      return deletedNode

    # if first node and there are more than one node in linked list! 
    elif self.head.value == value:
      deletedNode = self.head
      self.head = self.head.next
      self.tail.next = self.head
      return deletedNode

    # if last node.
    elif self.tail.value == value:
      deletedNode = self.tail
      prvNode = self.head
      for _, node in enumerate(self):
        if node.value == value:
           prvNode.next = self.head
           self.tail = prvNode
           self.tail.next = self.head
           return deletedNode
        prvNode = node

    # if node in the middle.
    else:
      prvNode = self.head
      for _, node in enumerate(self):
        if node.value == value: 
          deletedNode = node
          prvNode.next = deletedNode.next
          return deletedNode
        prvNode = node
    return 'Value is not available in the Linked List!'

  def traverseCSLL(self):
    if not self.head:
      return 'no linked list found'
    else:
      node = self.head
      while node:
        print(node.value)
        node = node.next
        if node == self.head:
          break

  def clear(self):
    self.head = None
    self.tail.next = None
    self.tail = None
    return 

# cSLinkedList = CSLinkedList()
# cSLinkedList.insertNode(1,0)
# cSLinkedList.insertNode(2,-1)
# cSLinkedList.insertNode(3,1)
# cSLinkedList.insertNode(40,2)
# print('before: ', cSLinkedList)
# cSLinkedList.deleteNodeByValue(1)
# cSLinkedList.deleteNodeByValue(2)
# print('before: ', cSLinkedList.tail.next.value, cSLinkedList.tail.value)
# print('after:', cSLinkedList)
# cSLinkedList.traverseCSLL()


# Doubly Linked List 
class DNode:
  def __init__(self, value=None) -> None:
    self.prev = None
    self.value = value
    self.next = None

class DoublyLL:
  def __init__(self) -> None:
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next
      
  def reverseIter(self):
    node = self.tail
    while node:
      print(node.value)
      # yield node.value
      node = node.prev

  def __str__(self) -> str:
    return str([node.value for node in self])
  
  
  def createDLL(self, value):
    node = DNode(value)
    self.head = node
    self.tail = node
    self._count = 0
    self._count += 1
    return node
  
  def insertDNode(self, value, location):
    newNode = DNode(value)
    self._count += 1
     # if first node and only one node in the linked list.
    if not self.head:
        self.createDLL(value)
    # if insert in the beginning.
    elif location == 0:
      self.head.prev = newNode
      newNode.prev = None
      newNode.next = self.head
      self.head = newNode
    # if insert in the last.
    elif location == -1:
      newNode.next = None
      newNode.prev = self.tail
      self.tail.next = newNode
      self.tail = newNode
      # if insert in the middle.
    else:
      for index, node in enumerate(self):
        if index == location - 1:
          prevNode = node
          nextNode = node.next
          prevNode.next = newNode
          nextNode.prev = newNode
          newNode.prev = prevNode
          newNode.next = nextNode
          break
  
  def find(self, value):
    for index, node in enumerate(self):
      if node.value == value:
        return index
    return 'there is no such value!'
  
  def __getitem__(self, index):
    for c_index, node in enumerate(self):
      if c_index == index:
        return node.value
    return 'there is no such value!'

  def __len__(self):
    return self._count
    


  def removeDNode(self, location):
    if not self.head:
      return 'Linked List does not exist!'
    self._count -= 1
    # if first or last and only one node in the linked list.
    if self.head == self.tail:
      deletedNode = self.head
      self.head = self.head.next
      self.tail = None
      return deletedNode
    # if first and has more than one node.
    elif location == 0:
      deletedNode = self.head
      self.head.next.prev = None
      self.head = self.head.next
      return deletedNode
    # if last and has more than one node.
    elif location == -1:
      deletedNode = self.tail
      self.tail.prev.next = None
      self.tail = self.tail.prev
      return deletedNode
    else:
      for index, node in enumerate(self):
        if index == location:
          deletedNode = node
          # if it's last node.
          if self.tail == node:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return deletedNode
          else:
            node.prev.next = node.next
            node.next.prev = node.prev
            return deletedNode
      return 'Node does not exist!'

  def clear(self):
    # coz they are pointing at each other.
    for node in self:
      node.prev = None
    self.head = None
    self.tail = None

# dLL = DoublyLL() 
# dLL.createDLL(1)
# dLL.insertDNode(3, -1)
# dLL.insertDNode(0, 0)
# dLL.insertDNode(0, 3)
# # dLL.removeDNode(0)    
# print('before: ', dLL)
# dLL.clear()
# print('after: ', dLL  )



# Circular Doubly Linked List
class CDoublyLL:
  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self._count = 0

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next
      if node == self.head:
        break
        
  def __str__(self) -> str:
    return str([node.value for node in self])

  def reverseIter(self):
    node = self.tail
    while node:
      print(node.value)
      node = node.prev
      if node == self.tail:
        break 

  def find(self, value):
    for index, node in enumerate(self):
      if node.value == value:
        return index
    return 'there is no such value!'
  
  def __getitem__(self, index):
    for c_index, node in enumerate(self):
      if c_index == index:
        return node.value
    return 'there is no such value!'

  def __len__(self):
    return self._count
    
  def createDLL(self, value):
    node = DNode(value)
    self.head = node
    self.tail = node
    node.next = node
    node.prev = node
    self._count += 1
    return node
  
  def insertDNode(self, value, location):
    newNode = DNode(value)
    self._count += 1
     # if first node and only one node in the linked list.
    if not self.head:
        self.createDLL(value)
    # if insert in the beginning.
    elif location == 0:
      self.head.prev = newNode
      newNode.prev = self.tail
      newNode.next = self.head
      self.head = newNode
      self.tail.next = newNode
      return newNode

    # if insert in the last.
    elif location == -1:
      newNode.next = self.head
      newNode.prev = self.tail
      self.head.prev = newNode
      self.tail.next = newNode
      self.tail = newNode
      return newNode
    # if insert in the middle.
    else:
      for index, prevNode in enumerate(self):
        if index == location - 1:
          nextNode = prevNode.next
          prevNode.next = newNode
          nextNode.prev = newNode
          newNode.prev = prevNode
          newNode.next = nextNode
          return newNode
      return 'index outside range!'

  def removeDNode(self, location):
    if not self.head:
      return 'Linked List does not exist!'
    self._count -= 1
    # if first or last and only one node in the linked list.
    if self.head == self.tail:
      deletedNode = self.head
      self.head.next = None
      self.head.prev = None
      self.head = None
      self.tail = None
      return deletedNode
    # if first and has more than one node.
    elif location == 0:
      deletedNode = self.head
      self.head.next.prev = self.tail
      self.tail.next = self.head.next
      self.head = self.head.next
      return deletedNode
    # if last and has more than one node.
    elif location == -1: 
      deletedNode = self.tail
      self.tail.prev.next = self.head
      self.head.prev = self.tail.prev
      self.tail = self.tail.prev
      return deletedNode
    else:
      for index, node in enumerate(self):
        if index == location:
          deletedNode = node
          # if it's last node.
          if self.tail == node:
            self.tail.prev.next = self.head
            self.head.prev = self.tail.prev
            self.tail = self.tail.prev
            return deletedNode
          else:
            node.prev.next = node.next
            node.next.prev = node.prev
            return deletedNode
      return 'Node does not exist!'

  def clear(self):
    # coz they are pointing at each other.
    for node in self:
      node.prev = None
    self.head.next = None
    self.tail.prev = None
    self.head = None
    self.tail = None

# cDLL = CDoublyLL()
# cDLL.createDLL(1)
# cDLL.insertDNode(2,0) 
# cDLL.insertDNode(4,1)
# newNode = cDLL.insertDNode(3,1 )
# newNode = cDLL.insertDNode(33,2 )

# print('before: ', cDLL)

# deleted = cDLL.clear()
# print('after: ', cDLL)
# print(cDLL.head.prev.value)

from random import randint
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield  current_node
            current_node = current_node.next

    def __len__(self):
        return self.len

    def __str__(self):
        return str([node.value for node in self])

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.len += 1

    @staticmethod
    def generate(n, min_value, max_value):
        ll = LinkedList()
        for _ in range(n):
            ll.add(randint(min_value, max_value))
        return ll

def removeDuplicates(ll):
  for _, node in enumerate(ll):
    c_node = node.next
    prevNode = node
    while c_node:
      if node.value == c_node.value:
        if c_node == ll.tail:
          prevNode.next = None
          ll.tail = prevNode
        else:
          prevNode.next  = c_node.next
        c_node = c_node.next
      else:
        prevNode = c_node
        c_node = c_node.next
  return ll

  

def removeMiddleNode(ll):
  prevNode = ll.head
  print((len(ll)//2)+1, len(ll))
  for index, node in enumerate(ll):
    if index == len(ll)//2:
      print('deleted node: ', node.value, 'index: ', index)
      prevNode.next = node.next
    prevNode = node
  return ll


def test(n, min, max, skargs = None):
    ll = LinkedList.generate(n, min, max)
    if skargs:
        t = {}
        for k in skargs:
            t[k] = str(skargs[k])
        print("Input Linked List: ", ll, ', ', t, '\n')
        start_time = time.time()
        ll = solution(ll, **skargs)
    else:
        print("Input Linked List: ", ll, '\n')
        start_time = time.time()
        ll = solution(ll)
    end_time = time.time() - start_time
    print("Output: ", ll, '\n')
    print("Execution Time in milliseconds: ", round(end_time * 1000, 3), '\n')
    print(''.join(['#' for _ in range(0, 30)]), '\n\n')

test(11, 0, 5)
# test(10, 0, 0)
# test(0, 0, 0)

# [1,4,3,2,5,2,1,2,1]
# [1,4,3,0,2,5,2]
# 3
# if value before x is less than it stays at the same place.
        # for Inode in checkList:
        #     node = head
        #     prevNode = head
        #     while node:
        #         if Inode.val < x and Inode.val < node.val:
        #             # if start at head.
        #             if node == head:
        #                 temp = head
        #                 head = Inode
        #                 head.next = temp
        #             # if last
        #             elif not node.next:
        #                 prevNode.next = Inode
        #             else:
        #                 Inode.next = prevNode.next
        #                 prevNode.next = Inode
        #             break
        #         prevNode = node
        #         node = node.next