## Floyd Algorithm implementation to check if list has loop
## Two pointes 1) First  : advancing by one node at a time
##             2) Second : Advancing by two nodes at a time
## wil meet at one node if there is a loop, else will end at None.
## Execution complexity = O(n), Space complexity O(1)

from random import randrange
from SingleLinkList import SingleLList

def getLoopNodeCount(ll):
    if ll.head == None:
        raise ValueError("Empty List!!")
    if ll.head == ll.head.getNext():
        return 1
    
    # First pointer
    if ll.head.getNext() != None:
        ptr1 = ll.head.getNext()
    else:
        return 0
    
    # Second pointer
    if ll.head.getNext().getNext() != None:
        ptr2 = ll.head.getNext().getNext()
    else:
        return 0

    while ptr1 != ptr2:
        if ptr1.getNext() != None:
            ptr1 = ptr1.getNext()
        else:
            return 0
        if ptr2.getNext().getNext() != None:
            ptr2 = ptr2.getNext().getNext()
        else:
            return 0

    ncount = 1
    ptr2 = ptr2.getNext()
    while ptr1 != ptr2:
        ptr2 = ptr2.getNext()
        ncount += 1
    
    return ncount

if __name__ == '__main__':
    ll = SingleLList()
    lladdress = []
    N = 10**6
    for i in range(N):
        ll.insertAtBeginning(randrange(10000))

    #ll.showSingleLL()
    try:
        nNode = ll.getNodeAtPos(N)
        nodeAtk = ll.getNodeAtPos(3000)
        #Create loop
        nNode.setNext(nodeAtk)
        print('Count: ', getLoopNodeCount(ll))
        #if nde != None:
        #    print(nde.getData())
        #else:
        #    print("List has no loop!!")
    except ValueError as v:
         print('Error:', v)

    #ll.showSingleLL()