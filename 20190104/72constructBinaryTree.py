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
    def buildTree(self, inorder, postorder):
        # write your code here
        if not inorder:
            return None

        # use -1 to get the last item of the postorder
        root = TreeNode(postorder[-1])
        position = inorder.index(root.val)

        root.left = self.buildTree(inorder[: position], postorder[: position])
        root.right = self.buildTree(inorder[position + 1: ], postorder[position: -1])

        return root
