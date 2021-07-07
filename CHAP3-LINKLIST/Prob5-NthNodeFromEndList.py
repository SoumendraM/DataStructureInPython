## List Implemenation of Stack
from random import randrange
from SingleLinkList import SingleLList



def nthNodeFromEnd(ll, n):
    ll.showSingleLL()    
    curr = ll.head
    for i in range(1,n):
        if curr == None:
            raise IndexError("List has < ", n, "elements")
        curr = curr.getNext()

    nFromLast = ll.head
    while curr.getNext() != None:
        curr = curr.getNext()
        nFromLast = nFromLast.getNext()

    return nFromLast.getData()

if __name__ == '__main__':
    ll = SingleLList()
    for i in range(50):
        ll.insertAtBeginning(randrange(100))
    print(nthNodeFromEnd(ll, 20)) 
