# A simplest implementation of hashing using Pyhton hash() function
# Assumes, there is no collision

from random import randrange
from SingleLinkList import SingleLList

class SimpleHash:
    def __init__(self, N):
        self.nSize = N
        self.arr = [None] * N

    def isHashed(self, obj):
        indx = hash(obj) % self.nSize
        if self.arr[indx] == 1:
            return True
        else:
            return False

    def hashIt(self, obj):
        indx = hash(obj) % self.nSize
        if self.arr[indx] == None:
            self.arr[indx] = 1

    def getHashKey(self, obj):
        return hash(obj) % self.nSize


if __name__ == '__main__':
    ll = SingleLList()
    lladdress = []
    N = 10**4
    for i in range(10):
        ll.insertAtBeginning(randrange(1000))

    ll.showSingleLL()

    hObj = SimpleHash(10000)

    t1 = ll.head
    t2 = ll.head.getNext()
    t3 = ll.head.getNext().getNext()

    hObj.hashIt(t1)
    hObj.hashIt(t2)
    hObj.hashIt(t3)

    t4 = ll.head.getNext().getNext().getNext().getNext()
    print("t1 hashKey:", hObj.getHashKey(t1))
    print("t2 hashKey:", hObj.getHashKey(t2))
    print("t3 hashKey:", hObj.getHashKey(t3))
    print("t4 hashKey:", hObj.getHashKey(t4))

    print("t1 hash:", hObj.isHashed(t1))
    print("t2 hash:", hObj.isHashed(t2))
    print("t3 hash:", hObj.isHashed(t3))
    print("t4 hash:", hObj.isHashed(t4))
