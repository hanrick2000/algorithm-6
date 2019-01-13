"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here

        # method 1: Divide & Conquer
        if not lists:
            return None

        return self.mergeHelper(lists, 0, len(lists) - 1)

    def mergeHelper(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2

        leftList = self.mergeHelper(lists, start, mid)
        rightList = self.mergeHelper(lists, mid + 1, end)

        return self.mergeLists(leftList, rightList)

    def mergeLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            else:
                tail.next = list2
                tail = list2
                list2 = list2.next

        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
