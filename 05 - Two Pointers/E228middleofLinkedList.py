"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        if head is None:
            return head

        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

# ========  leetcode ======== #
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         if head is None:
#             return head
#
#         slow, fast = head, head.next
#         while fast is not None and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next
#
#         if fast is not None:
#             slow = slow.next
#
#         return slow
