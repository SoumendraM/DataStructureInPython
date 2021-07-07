## Plain Node implementation

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

## Single Linked List inplementation
class SingleLList():
    def __init__(self):
        self.head = None
        self.length = 0

    ## Auxilliary Functions
    def listLength(self):
        current = self.head

        length = 0
        while current != None:
            length += 1
            current = current.next
        return length

    ## Insertions

    def insertAtBeginning(self, data):
        #Construct new node
        node = Node()
        node.setData(data)
        node.setNext(None)
        
        if self.length == 0:
            self.head = node
        else:
            node.setNext(self.head)
            self.head = node
        
        self.length = self.length+1

    def insertAtEnd(self, data):
        node = Node()
        node.setData(data)
        node.setNext(None)

        if self.length == 0:
            self.head = node
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()

            current.setNext(node)
        
        self.length += 1
    
    def insertAtPos(self, pos, data):
        #Check pos range
        if pos <= 0 or pos > self.length:
            raise IndexError("Index out of range:",pos)
        else:
            if pos == 1:
                self.insertAtBeginning(data)
            else:
                #if pos == self.length:
                #    self.insertAtEnd(data)
                #else:
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

    ## Deletions
    def deleteFromBeginning(self):
        if self.length == 0:
            raise Exception("List Empty")
            return 
        else:
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

    def deleteNodeFromList(self, node):
        if node == None:
            raise ValueError("Node is empty")
        else:
            if self.length == 0:
                raise ValueError("List is empty")
            else:
                if self.head == node: # head to be deleted
                    self.head = self.head.getNext()
                    self.length -= 1
                    return

                current = self.head
                parent = current

                while current != None:
                    if current == node:
                        if current.getNext() == None:
                            parent.setNext(None)
                        else:
                            parent.setNext(current.getNext())
        
                        self.length -= 1
                        return
                    parent = current
                    current = current.getNext()
                
                raise ValueError("Node not found in the group")

    def deleteValfromList(self, val):
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
    def showSingleLL(self):
        if self.length != 0:
            current = self.head
            while current != None:
                print(current.getData(), end = ' ')
                current = current.getNext() 
            print(end = '\n')
        else:
            raise Exception("List is Empty")