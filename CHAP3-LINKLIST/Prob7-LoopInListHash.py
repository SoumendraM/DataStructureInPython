## Hash based implementation implementation to check if list has loop
## If list has loop the next points of 2 of the nodes
## will point to the same next node - has same next pointer
## Execution complexity = O(n)

from random import randrange
from SingleLinkList import SingleLList
from SimpleHash import SimpleHash

def listHasLoop(ll):
    hs = SimpleHash(10000000)
    curr = ll.head
    cnt = 0
    while curr.getNext() != None:
        cnt += 1
        #print(curr.getData())
        #print("curr:", curr, "hash:", hash(curr))
        if hs.isHashed(curr) != True:
            hs.hashIt(curr)
        else:
            #Double occurance in hash table
            #print("Count:", cnt)
            return True
        curr = curr.getNext()
        
    #print("Count:", cnt)
    return False

if __name__ == '__main__':
    ll = SingleLList()
    lladdress = []
    N = 10**4
    for i in range(N):
        ll.insertAtBeginning(randrange(1000))
    
    #ll.showSingleLL()
    nNode = ll.getNodeAtPos(5000)
    nodeAtk = ll.getNodeAtPos(1435)
    nNode.setNext(nodeAtk)
    listHasLoop(ll) 

    #ll.showSingleLL()