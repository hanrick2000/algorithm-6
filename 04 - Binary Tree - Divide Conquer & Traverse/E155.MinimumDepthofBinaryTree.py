"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0

        left = 0
        if root.left:
            left = self.minDepth(root.left)
        else:
            return self.minDepth(root.right) + 1

        right = 0
        if root.right:
            right = self.minDepth(root.right)
        else:
            return left + 1

        return min(left, right) + 1

    #     return self.helper(root)
    #
    # def helper(self, root):
    #     if root is None:
    #         return 0
    #
    #     left = 0
    #     if root.left:
    #         left = self.helper(root.left)
    #     else:
    #         return self.helper(root.right) + 1
    #
    #     right = 0
    #     if root.right:
    #         right = self.helper(root.right)
    #     else:
    #         return left + 1
    #
    #     return min(left, right) + 1
