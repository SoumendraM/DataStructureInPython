from random import randrange
from SingleLinkList import SingleLList

def insIntoSortedList(ll, num):
    if ll.head == None:
        raise ValueError("Empty List!!")

    curr = ll.head
    if ll.head.getData() >= num:
        ll.insertAtBeginning(num)
        return

    par = curr
    curr = curr.getNext()
    cnt = 2
    while curr != None:
        if curr.getData() >= num:
            ll.insertAtPos(cnt, num)
            return
        par = curr
        curr = curr.getNext()
        cnt += 1
    
    ll.insertAtEnd(num)
            

if __name__ == '__main__':
    ll = SingleLList()
    lladdress = []
    N = 10
    ve = 1
    for i in range(2, N+1):
        ve *= -1
        ll.insertAtEnd(i*i -1*ve)

    ll.showSingleLL()
    try:
        num = 121
        insIntoSortedList(ll, num)
        ll.showSingleLL()
    except ValueError as v:
         print('Error:', v)

    #ll.showSingleLL()