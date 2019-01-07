"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        return self.maxDepth(root)[1]

    def maxDepth(self, root):
        if not root:
            return 0, True

        left, isBalanced = self.maxDepth(root.left)
        if not isBalanced:
            return -1, False

        right, isBalanced = self.maxDepth(root.right)
        if not isBalanced:
            return -1, False

        if abs(left - right) > 1:
            return -1, False

        return max(left, right) + 1, True
