"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here

        # method 2:
        if not head:
            return head

        prevNode, currNode = None, head
        while currNode:
            nextNode, currNode.next = currNode.next, prevNode
            prevNode, currNode = currNode, nextNode

        return prevNode

        # method 1:
        # if not head or not head.next:
        #     return head

        # nextNode = self.reverse(head.next)
        # head.next.next = head
        # head.next = None

        # return nextNode
