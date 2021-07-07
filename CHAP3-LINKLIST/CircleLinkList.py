## Circular Link List implementation

## Circular List Node implementation

class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def hasNext(self):
        return self.next != None

## Circular Linked List inplementation
class CircleLList():
    def __init__(self):
        self.head = None
        self.length = 0

    ## Auxilliary Functions
  
    def listLength(self):
        current = self.head

        length = 0
        if current != None: length += 1
        while current.getNext() != self.head:
            length += 1
            current = current.getNext()
        return length

    ## Insertions

    def insertAtBeginning(self, data):
        #Construct new node
        node = Node()
        node.setData(data)
        node.setNext(None)
        
        if self.length == 0:
            self.head = node
            node.setNext(node) #head points to itself
        else:
            if self.length == 1:
                #reset head pointer
                node.setNext(self.head)
                self.head.setNext(node)
                self.head = node
            else: #Circular List with more than 2 nodes
                #Get the tail node   
                current = self.head.getNext()
                while current.getNext() != self.head:
                    current = current.getNext()

                node.setNext(self.head)
                self.head = node
                current.setNext(node)
        
        self.length = self.length+1

    def insertAtEnd(self, data):
        node = Node()
        node.setData(data)
        node.setNext(None)

        if self.length == 0:
            self.head = node
            node.setNext(node)
        else:
            current = self.head
            while current.getNext() != self.head:
                current = current.getNext()

            node.setNext(self.head)
            current.setNext(node)
        
        self.length += 1
    
    """
    def insertAtPos(self, pos, data):
        #Check pos range
        if pos <= 0 or pos > self.length:
            raise IndexError("Index out of range:",pos)
        else:
            if pos == 1:
                self.insertAtBeginning(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    node = Node()
                    node.setData(data)
                    node.setNext(None)

                    current = self.head
                    count = 2
                    while count < pos:
                        current = current.getNext()
                        count += 1
                    
                    node.setNext(current.getNext())
                    current.setNext(node)

                    self.length += 1
    """

    ## Deletions
    def deleteFromBeginning(self):
        if self.length == 0:
            raise Exception("List Empty")
        else:
            if self.length == 1:
                self.head = None
            else:
                current = self.head
                while (current.getNext() != self.head):
                    current = current.getNext()

                current.setNext(self.head.getNext())
                self.head = self.head.getNext()
            
            self.length -= 1

    def deleteFromEnd(self):
        if self.length == 0:
            return
        else:
            current = self.head
            parent = current
            while current.getNext() != None:
                parent = current
                current = current.getNext()
            
            parent.setNext(None)
            self.length -= 1
    
    """
    def deleteFromPos(self, pos):
        if pos <= 0 or pos > self.length:
            raise IndexError("Index out of range:", pos)
        else:
            current = self.head
            parent = current
            count = 1
            while count < pos:
                parent = current
                current = current.getNext()
                count += 1
            
            parent.setNext(current.getNext())
            self.length -= 1
    """

    def deleteNodeFromList(self, node):
        if node == None:
            raise ValueError("Node is empty")
        else:
            if self.length == 0:
                raise ValueError("List is empty")
            else:
                if self.listLength() == 1:
                    if self.head == node:
                        self.head = None
                        self.length -= 1
                    else:
                        print("Node not found!!!")
                else:
                    if self.listLength() == 2:
                        if self.head == node:
                            self.head = self.head.getNext()
                            self.head.setNext(self.head)
                            self.length -= 1
                        else:
                            if self.node.getNext() == node:
                                self.head.setNext(self.head)
                                self.length -= 1
                            else:
                                print("Node not found!!!")
                    else:
                        current = self.head

                        if current == node: # head node hit
                            while current.getNext() != self.head:
                                current = current.getNext()
                            self.head = self.head.getNext()
                            current.setNext(self.head)
                            return
                        else:
                            current = current.getNext()
                            parent = current
                            while current != self.head:
                                if current == node:
                                    parent.setNext(current.getNext())
                    
                                    self.length -= 1
                                    return
                                parent = current
                                current = current.getNext()
                    
                    print("Node not found in the group")

    def deleteValfromList(self, val): ## TBD
        if val == None:
            raise ValueError("Value not defined")
        else:
            if self.length == 0:
                raise ValueError("List is Empty")
            else:
                if self.head.getData() == val:
                    self.head = self.head.getNext()
                    self.length -= 1
                    return

                current = self.head
                parent = current 

                while current != None:
                    if current.getData() == val:
                        if current.getNext() == None:
                            parent.setNext(None)
                        else:    
                            parent.setNext(current.getNext())
                        self.length -= 1
                        return
                    parent = current
                    current = current.getNext()
                
                raise ValueError("Val", val, "not found in List.")

    def getNodeAtPos(self, pos):
        if pos <= 0 or pos > self.length:
            raise IndexError("Index out of range:", pos)

        count = 1
        current = self.head
        while count < pos:
            current = current.getNext() 
            count += 1

        return current        
                    
    def clearList(self):
        self.length = 0
        self.head = None

    # Auxilliary Funstions
    def showCircleLL(self):
        if self.length != 0:
            current = self.head
            print(current.getData(), end = ' ')
            while current.getNext() != self.head:
                current = current.getNext()
                print(current.getData(), end = ' ')
            print(end = '\n')
        else:
            raise Exception("List is Empty")