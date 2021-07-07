## Brute Force implementation to check if list has loop
## If list has loop the next points of 2 of the nodes
## will point to the same next node - has same next pointer
## Execution complexity = O(n^^2)

from random import randrange
from SingleLinkList import SingleLList

def checkList(ladd, node):
    for addrs in ladd:
        if addrs == node:
            return True
    return False

def listHasLoop(ll):
    lladdress = []
    curr = ll.head
    while curr != None:
        if checkList(lladdress, curr) == False:
            lladdress.append(curr)
            curr = curr.getNext()
        else:
            return True
    return False

if __name__ == '__main__':
    ll = SingleLList()
    lladdress = []
    N = 10**4
    for i in range(N):
        ll.insertAtBeginning(randrange(1000))
    
    #ll.showSingleLL()
    nNode = ll.getNodeAtPos(7746)
    nodeAtk = ll.getNodeAtPos(1435)
    nNode.setNext(nodeAtk)
    listHasLoop(ll) 

    #ll.showSingleLL()