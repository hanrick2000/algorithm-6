"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if not head:
            return head

        slow, fast, ismeet = head, head.next, False

        while fast is not None and fast.next is not None:
            if ismeet:
                if slow.val == fast.val:
                    return slow

                fast = fast.next
            else:
                if slow.val == fast.val:
                    ismeet = True
                    # slow goes back to the head and fast only moves one step
                    slow = head
                    fast = fast.next
                    continue

                fast = fast.next.next

            slow = slow.next

        return None
