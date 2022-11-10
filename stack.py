class Node:
  def __init__(self, value=None) -> None:
    self.value = value
    self.next = None

class LinkedList:
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

  def add(self, value):
    newNode = Node(value)
    if self.head == None:
      self.head = newNode
      self.tail = newNode
    else:
      newNode.next = self.head
      self.head = newNode

  def remove(self):
    deleted  = self.head
    if self.head == self.tail:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
    return deleted.value

  def headValue(self):
    return self.head.value


  def clear(self):
    self.head = None
    self.tail = None
    return 

class Stack:
  def __init__(self) -> None:
    self.list = LinkedList()

  def __str__(self) -> str:
    values = [str(node.value) for node in self.list]
    values = '\n'.join(values)
    return values

  def isEmpty(self):
    if self.list.head == None: return True
    else: return False

  def push(self, value):
    self.list.add(value)

  def pop(self):
    if self.isEmpty():
      return 'The Stack is empty!'
    else:
      return self.list.remove()
      
  def peek(self):
    return self.list.headValue()

  def delete(self):
    self.list.clear()
       

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.delete())
# print('removed: ',stack.pop())
print(stack)
