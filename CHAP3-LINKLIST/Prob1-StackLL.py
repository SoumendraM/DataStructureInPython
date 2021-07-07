## List Implemenation of Stack
from random import randrange

from SingleLinkList import SingleLList

class Stack:
    def __init__(self):
        self.ll = SingleLList()

    def getSize(self):
        return self.ll.listLength()

    def isEmpty(self):
        return self.ll.listLength() == 0

    def top(self):
        return self.ll.head.getData()

    def pop(self):
        val = self.ll.head.getData()
        self.ll.deleteFromBeginning()
        return val

    def push(self, val):
        self.ll.insertAtBeginning(val)

    ## Auxilliary
    def printStack(self):
        self.ll.showSingleLL()

def testStack():
    ss = Stack()

    for i in range(10):
        ss.push(randrange(100))

    ss.printStack()
    print("Top:", ss.top())
    ss.printStack()
    print("Pop:", ss.pop())
    ss.printStack()
    print("Pop:", ss.pop())
    ss.printStack()
    print("Pop:", ss.pop())
    ss.printStack()
    print("IsEmpty:", ss.isEmpty())
    ss.printStack()
    print("Push:", 71) 
    ss.push(71)
    ss.printStack()
    print("Push:", 201) 
    ss.push(201)
    ss.printStack()
    print("Size:", ss.getSize())
    ss.printStack()

    for i in range(10):
        print("Pop:", ss.pop())
        ss.printStack()

if __name__ == '__main__':
    testStack()
