"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here

        # method two:morris
        result = []

        currNode = None
        while root is not None:
            if root.left is not None:
                currNode = root.left

                while currNode.right is not None and currNode.right is not root:
                    currNode = currNode.right

                if currNode.right is root:
                    result.append(root.val)
                    currNode.right = None
                    root = root.right
                else:
                    currNode.right = root
                    root = root.left
            else:
                result.append(root.val)
                root = root.right

        return result

    #     # method one: traverse
    #     result = []
    #     self.traverse(root, result)

    #     return result

    # def traverse(self, root, result):
    #     if root is None:
    #         return

    #     self.traverse(root.left, result)
    #     result.append(root.val)
    #     self.traverse(root.right, result)
