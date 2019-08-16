"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here

        # method 2:
        # if not root:
        #     return root

        # queue = [root]
        # while queue:
        #     node = queue.pop()
        #     node.left, node.right = node.right, node.left

        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)

        # return root

        # method 1:
        # if not root:
        #     return root

        # leftnode = root.left
        # root.left, root.right = root.right, leftnode

        # self.invertBinaryTree(root.left)
        # self.invertBinaryTree(root.right)

        # return root

        # method 3:
        if not root:
            return root

        root.left, root.right = self.invertBinaryTree(root.right), self.invertBinaryTree(root.left)
        return root
