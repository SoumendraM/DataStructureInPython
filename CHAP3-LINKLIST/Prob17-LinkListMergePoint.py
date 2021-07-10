"""
Suppose there arc lwo singly linked lists both of which inlerscct at some point and become a
single linked list. The head or start pointers of both the lists are known, but the intersecting node is not
known. Also, the number of nodes in each of the lists before they intersect is unknown and may be different
in each list. list I may have n nodes before it reaches the intersection point, and list 2. might have m nodes
before it reaches the intcrsecl ion point where m and n mny be m = n, m < n or m > n. Give an algorithm for
finding the merging point.
Returns the merger point node.
"""

from random import randrange
from SingleLinkList import SingleLList
from SimpleHash import SimpleHash

def mergePointLinkList(ll1, ll2):
    if ll1.head == None or ll2.head == None:
        raise ValueError("Empty List!!")

    hs = SimpleHash(10000)
    curr1 = ll1.head
    curr2 = ll2.head

    while curr1.getNext() != None:
        hs.hashIt(curr1)
        curr1 = curr1.getNext()
    
    while curr2.getNext() != None:   
        if hs.isHashed(curr2) == True:
            return curr2
        curr2 = curr2.getNext()    
 
    return None

if __name__ == '__main__':
    ll1 = SingleLList()

    for i in range(10):
        ll1.insertAtBeginning(i)

    ll1.showSingleLL()

    ll2 = SingleLList()

    for i in range(10):
        ll2.insertAtBeginning(i*2 + 100)

    #ll2.insertNodeAtEnd(ll1.getNodeAtPos(6))    
    ll2.showSingleLL()
    
    try:
        nde = mergePointLinkList(ll2, ll1)
        if nde != None:
            print(nde.getData(), nde)
        else:
            print("Lists are not merged!!!")
    except ValueError as v:
         print('Error:', v)

