from SingleLinkList import SingleLList
from random import randrange


def testSLL():
    ll = SingleLList()

    for i in range(10):
        ll.insertAtBeginning(i)

    print(ll.listLength())
    ll.showSingleLL()

    """for i in range(10):
        ll.deleteFromPos(randrange(10))
        ll.showSingleLL()
    """
    ##print(ll.getNodeAtPos(11).getData())
    #ll.deleteNodeFromList(ll.getNodeAtPos(1))
    ll.deleteValfromList(0)

    print(ll.listLength())
    ll.showSingleLL()

    ll.clearList()
    print(ll.listLength())
    ll.showSingleLL()

if __name__ == '__main__':
    testSLL()