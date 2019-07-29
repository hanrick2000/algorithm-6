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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here

        # method two: divide conquer
        return self.divideConquer(root)[0]

    def divideConquer(self, root):
        if root is None:
            return True, None, None

        # leftNode
        isBST, maxNode, leftMinNode = self.divideConquer(root.left)
        if not isBST:
            return False, None, None

        # rightNode
        isBST, rightMaxNode, minNode = self.divideConquer(root.right)
        if not isBST :
            return False, None, None

        if (maxNode is not None and maxNode.val >= root.val) or (minNode is not None and minNode.val <= root.val):
            return False, None, None

        if rightMaxNode is None:
            maxNode = root
        else:
            maxNode = rightMaxNode
        if leftMinNode is None:
            minNode = root
        else:
            minNode = leftMinNode

        return True, maxNode, minNode

    #     # method one: traverse
    #     self.lastNode = None
    #     self.isBST = True

    #     self.inorderTraverse(root)

    #     return self.isBST

    # def inorderTraverse(self, root):
    #     if not root or not self.isBST:
    #         return

    #     self.inorderTraverse(root.left)

    #     if self.lastNode is not None and self.lastNode.val >= root.val:
    #         self.isBST = False
    #         return
    #     self.lastNode = root

    #     self.inorderTraverse(root.right)
