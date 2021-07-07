from random import randrange
from SingleLinkList import SingleLList

def reverseLinkList(ll):
    if ll.head == None:
        raise ValueError("Empty List!!")

    curr = ll.head

    par = curr
    curr = curr.getNext()

    par.setNext(None)
    while curr != None:
        tmp = curr.getNext()
        curr.setNext(par)
        par = curr
        curr = tmp
    
    ll.head = par

           

if __name__ == '__main__':
    ll = SingleLList()
    lladdress = []
    N = 10 ** 3
    ve = 1
    for i in range(2, N+1):
        ve *= -1
        ll.insertAtEnd(i*i -1*ve)

    #ll.showSingleLL()
    try:
        reverseLinkList(ll)
        #ll.showSingleLL()
    except ValueError as v:
         print('Error:', v)

    #ll.showSingleLL()