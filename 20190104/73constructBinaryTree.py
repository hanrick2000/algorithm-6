"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        # if only judge inorder is None, then can't check inorder is [].
        if not inorder:
            return None

        root = TreeNode(preorder[0])
        position = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: position + 1], inorder[: position])
        root.right = self.buildTree(preorder[position + 1:], inorder[position + 1:])

        return root
