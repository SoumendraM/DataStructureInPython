from DoubleLinkList import DoubleLList
from random import randrange


def testDLL():
    ll = DoubleLList()

    for i in range(20):
        ll.insertAtBeginning(randrange(100))

    print(ll.listLength())
    ll.showDoubleLL()

    ll.insertAtPos(17, 100)

    #ll.deleteFromPos(4)
    """
    for i in range(10):
        ll.deleteFromPos(randrange(8))
        ll.showDoubleLL()
    """
    #print(ll.getNodeAtPos(4).getData())
    #ll.deleteNodeFromList(ll.getNodeAtPos(4))
    #ll.deleteValfromList(0)

    #print(ll.listLength())
    #ll.showSingleLL()

    #ll.clearList()
    print(ll.listLength())
    ll.showDoubleLL()

if __name__ == '__main__':
    testDLL()