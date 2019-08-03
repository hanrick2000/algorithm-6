"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    last_node = None
    
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here

        # method 2:
        if root is None:
            return None

        if self.last_node is not None:
            self.last_node.left = None
            self.last_node.right = root

        self.last_node, right_node = root, root.right

        self.flatten(root.left)
        self.flatten(right_node)

    #     # method 1:
    #     self.helper(root)
    #
    # def helper(self, root):
    #     if root is None:
    #         return None
    #
    #     print(root.val)
    #     left_last, right_last = self.helper(root.left), self.helper(root.right)
    #
    #     if left_last is not None:
    #         left_last.right, root.right, root.left = root.right, root.left, None
    #
    #     if right_last is not None:
    #         return right_last
    #
    #     if left_last is not None:
    #         return left_last
    #
    #     return root
