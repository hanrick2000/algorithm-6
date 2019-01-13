"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        reSize = 2 * len(hashTable)
        reHashTable = [None] * reSize

        for item in hashTable:
            while item is not None:
                self.addToReHashTable(reHashTable, item)
                item = item.next

        return reHashTable

    def addToReHashTable(self, hashTable, item):
        index = item.val % len(hashTable)

        node = ListNode(item.val)
        if hashTable[index] is not None:
            linkList = hashTable[index]
            while linkList.next is not None:
                linkList = linkList.next
            linkList.next = node
        else:
            hashTable[index] = node
            
