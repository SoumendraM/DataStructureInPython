from CircleLinkList import CircleLList
from random import randrange


def testCLL():
    ll = CircleLList()

    for i in range(10):
        ll.insertAtBeginning(i)
        #ll.insertAtBeginning(randrange(100))

    print(ll.listLength())
    ll.showCircleLL()

    ll.insertAtEnd(100)
    ll.insertAtBeginning(101)    

    print("Length:", ll.listLength())
    ll.showCircleLL()
    print("-----------------")

    print(ll.getNodeAtPos(6).getData())
    ll.deleteNodeFromList(ll.getNodeAtPos(6))
    ll.showCircleLL()
    print("Length:", ll.listLength())
    ll.deleteNodeFromList(ll.getNodeAtPos(1))
    ll.showCircleLL()
    print("Length:", ll.listLength())
    ll.deleteNodeFromList(ll.getNodeAtPos(ll.listLength()-1))
    ll.showCircleLL()
    print("Length:", ll.listLength())
    ll.deleteNodeFromList(ll.getNodeAtPos(ll.listLength()))
    """
    count = 0
    while count < 12:
        ll.showCircleLL()
        print("Length:", ll.listLength())
        ll.deleteFromBeginning()
        count += 1
    """

    ll.showCircleLL()
    print("Length:", ll.listLength())

    #ll.clearList()

if __name__ == '__main__':
    testCLL()