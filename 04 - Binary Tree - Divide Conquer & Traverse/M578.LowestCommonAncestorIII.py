"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        lca, a, b = self.helper(root, A, B)

        if a and b:
            return lca

        return None

    def helper(self, root, A, B):
        if root is None:
            return None, False, False

        left_node, left_a, left_b = self.helper(root.left, A, B)
        right_node, right_a, right_b = self.helper(root.right, A, B)

        a = left_a or right_a or root == A
        b = left_b or right_b or root == B

        if root == A or root == B or (left_node is not None and right_node is not None):
            return root, a, b

        if left_node is not None:
            return left_node, a, b

        if right_node is not None:
            return right_node, a, b

        return None, a, b
