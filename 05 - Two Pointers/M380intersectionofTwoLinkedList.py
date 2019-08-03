"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if not headA or not headB:
            return None

        # first, find the last node of the headA
        node = headA
        while node.next is not None:
            node = node.next

        # link the tail to the top of the headB, then becomes a cycle
        node.next = headB
        result = self.detectCycle(headA)
        # disconnect with headB
        node.next = None

        return result

    def detectCycle(self, head):
        slow, fast, isMeet = head, head.next, False

        while fast is not None and fast.next is not None:
            if slow.val == fast.val:
                if isMeet:
                    return slow
                else:
                    isMeet = True
                    slow = head
                    fast = fast.next
                    continue

            if isMeet:
                fast = fast.next
            else:
                fast = fast.next.next

            slow = slow.next
        return None
