"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def isSubtree(self, T1, T2):
        # write your code here
        if not T2:
            return True
        if not T1:
            return False

        stack = [T1]
        while stack:
            root = stack.pop()
            if self.isSame(root, T2):
                return True

            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return False

    def isSame(self, T1, T2):
        if not T1 and not T2:
            return True

        if not T1 or not T2 or T1.val != T2.val:
            return False

        return self.isSame(T1.left, T2.left) and self.isSame(T1.right, T2.right)
        
