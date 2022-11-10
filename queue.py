class DynamicQueue:
  def __init__(self) -> None:
    self.queue = []

  def __str__(self) -> str:
    values = [str(item) for item in self.queue]
    values = ' <- '.join(values)
    return values
  
  def isEmpty(self):
    if len(self.queue) == 0: return True 
    else: return False

  def enQueue(self, value):
    self.queue.append(value)

  def deQueue(self):
    deleted = self.queue[0]
    del self.queue[0]
    return deleted
  
  def delete(self):
    self.queue = []
 

class FixedQueue:
    def __init__(self, size):
        self.size = size
        self.list = size * [None]
        self.start = -1
        self.top = -1

    def __str__(self):
        return ' <== '.join([f"|s|{item}|s|"if index == self.start % self.size else f"|t|{item}|t|"if index == self.top % self.size else str(item) for index, item in enumerate(self.list)])

    
    def enQueue(self, value):
        if self.isFull():
            raise Exception("Queue is Full")
        self.start += 1
        self.list[self.start % self.size] = value
        if self.top == -1:
            self.top = 0

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")
        value = self.list[self.top % self.size]
        self.list[self.top % self.size] = None
        self.top += 1
        return value

    def peek(self):
        if self.isEmpty():
            raise Exception('Queue is Empty')
        return self.list[self.top % self.size]

    def isFull(self):
        return self.start - self.top == self.size - 1

    def isEmpty(self):
        return self.top == self.start == -1 or self.top > self.start

    def delete(self):
        self.list = self.size * [None]
        self.start = -1
        self.top = -1
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

  def __str__(self): 
      return str([node.value for node in self])

  def add(self, value):
    newNode = Node(value)
    if self.head == None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode

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
class LLQueue:
  def __init__(self) -> None:
    self.queue = LinkedList()
  
  def __str__(self) -> str:
    values = [str(node.value) for node in self.queue]
    values = ' <- '.join(values)
    return values
  
  def isEmpty(self):
    if self.queue.head == None: return True
    else: return False

  def enQueue(self, value):
    self.queue.add(value)

  def deQueue(self):
    if self.isEmpty(): raise  Exception('The queue is empty!')
    else:
      return self.queue.remove()

  def peek(self):
    return self.queue.headValue()

  def delete(self):
    self.queue.clear()  


class MultiStack:
  def __init__(self, stackSize) -> None:
      self.numberStacks = 3
      self.custList = [0] * (stackSize * self.numberStacks)
      self.sizes = [0] * self.numberStacks
      self.stackSize = stackSize

  def __str__(self) -> str:
    values = ''
    stackNumber = 0
    for i in range(len(self.custList)):
      if i % self.stackSize == 0:
        stackNumber += 1 
        values += f'Stack Number {stackNumber}\n' 
      values += f'{i} \n'
    return values

  def isEmpty(self):
    print(self.custList)
    for i in range(self.numberStacks):
      if len(self.custList[i]) > 3: return False
    return True





queue = MultiStack(4)
# queue.enQueue(1)
# queue.enQueue(2)
# queue.enQueue(3)
# queue.enQueue(4)
print(queue.isEmpty())
# print('dequeue: ', queue.deQueue())
# print('dequeue: ', queue.deQueue())
# print('dequeue: ', queue.deQueue())
# queue.enQueue(5)
# print(queue)
# queue.enQueue(6)
# # print('peek: ', queue.peek())
# print(queue)
    # def __init__(self):
    #     self.stack = []
    #     self.mins = []
    #     self.offset = -1
        
        
    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if self.mins == []: self.mins.append(val)
    #     elif self.mins[-1] >= val: self.mins.append(val)
    #     self.offset += 1
                    
    # def pop(self) -> None:
    #     if self.mins[-1] == self.stack[self.offset]:
    #         self.mins.pop()
    #     self.stack.pop()
    #     self.offset -= 1
        

    # def top(self) -> int:
    #     return self.stack[self.offset]
        

    # def getMin(self) -> int:
    #     return self.mins[-1]