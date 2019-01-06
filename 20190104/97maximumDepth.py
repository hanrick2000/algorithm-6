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
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here

        # method one: Divide Conquer
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

    #     # method two: traverse
    #     self.depth = 0
    #     self.traverse(root, 1)

    #     return self.depth

    # def traverse(self, root, currDepth):
    #     if not root:
    #         return

    #     self.depth = max(self.depth, currDepth)

    #     self.traverse(root.left, currDepth + 1)
    #     self.traverse(root.right, currDepth + 1)
