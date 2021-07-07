## Floyd Algorithm implementation to check if list has loop
## Two pointes 1) First  : advancing by one node at a time
##             2) Second : Advancing by two nodes at a time
## wil meet at one node if there is a loop, else will end at None.
## Execution complexity = O(n), Space complexity O(1)

from random import randrange
from SingleLinkList import SingleLList

def listHasLoop(ll):
    if ll.head == None:
        raise ValueError("Empty List!!")
    if ll.head == ll.head.getNext():
        return ll.head
    
    # First pointer
    if ll.head.getNext() != None:
        ptr1 = ll.head.getNext()
    else:
        return None
    
    # Second pointer
    if ll.head.getNext().getNext() != None:
        ptr2 = ll.head.getNext().getNext()
    else:
        return None

    while ptr1 != ptr2:
        if ptr1.getNext() != None:
            ptr1 = ptr1.getNext()
        else:
            return None
        if ptr2.getNext().getNext() != None:
            ptr2 = ptr2.getNext().getNext()
        else:
            return None

    return ptr1

if __name__ == '__main__':
    ll = SingleLList()
    lladdress = []
    N = 10**4
    for i in range(N):
        ll.insertAtBeginning(randrange(10000))
    #ll.insertAtBeginning(1)
    #ll.insertAtBeginning(2)
    #ll.getNodeAtPos(1).setNext(ll.getNodeAtPos(1))
    #ll.showSingleLL()
    try:
        nNode = ll.getNodeAtPos(7564)
        nodeAtk = ll.getNodeAtPos(2546)
        nNode.setNext(nodeAtk)
        nde = listHasLoop(ll)
        if nde != None:
            print(nde.getData())
        else:
            print("List has no loop!!")
    except ValueError as v:
         print('Error:', v)

    #ll.showSingleLL()