"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        # Divide Conquer
        minimum, tree, sum = self.helper(root)

        return tree

    def helper(self, root):
        if root is None:
            return sys.maxsize, None, 0

        left_min, left_tree, left_sum = self.helper(root.left)
        right_min, right_tree, right_sum = self.helper(root.right)

        sum = left_sum + right_sum + root.val
        minimum = min(left_min, right_min, sum)

        if left_min == minimum:
            return left_min, left_tree, sum

        if right_min == minimum:
            return right_min, right_tree, sum

        return sum, root, sum
