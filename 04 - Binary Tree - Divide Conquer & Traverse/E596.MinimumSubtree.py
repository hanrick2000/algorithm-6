"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    min_val, min_node = sys.maxsize, None
    
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        # Divide Conquer
        # method 2
        self.helper(root)

        return self.min_node

    def helper(self, root):
        if root is None:
            return 0

        left_sum, right_sum = self.helper(root.left), self.helper(root.right)
        sum = left_sum + right_sum + root.val

        if self.min_node is None or self.min_val > sum:
            self.min_node, self.min_val = root, sum

        return sum

        # method 1
    #     minimum, tree, sum = self.helper(root)

    #     return tree

    # def helper(self, root):
    #     if root is None:
    #         return sys.maxsize, None, 0

    #     left_min, left_tree, left_sum = self.helper(root.left)
    #     right_min, right_tree, right_sum = self.helper(root.right)

    #     sum = left_sum + right_sum + root.val
    #     minimum = min(left_min, right_min, sum)

    #     if left_min == minimum:
    #         return left_min, left_tree, sum

    #     if right_min == minimum:
    #         return right_min, right_tree, sum

    #     return sum, root, sum
