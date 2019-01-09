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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here

        # method three: do not use recursion
        result = []
        if root is None:
            return result

        stack = [root]

        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return result

        # # method two: morris
        # result = []
        # currNode = None

        # while root is not None:
        #     if root.left is not None:
        #         currNode = root.left

        #         while currNode.right is not None and currNode.right is not root:
        #             currNode = currNode.right

        #         if currNode.right is root:
        #             currNode.right = None
        #             root = root.right
        #         else:
        #             result.append(root.val)
        #             currNode.right = root
        #             root = root.left
        #     else:
        #         result.append(root.val)
        #         root = root.right

        # return result

    #     # method one: traverse
    #     result = []
    #     self.traverse(root, result)

    #     return result

    # def traverse(self, root, result):
    #     if root is None:
    #         return

    #     result.append(root.val)
    #     self.traverse(root.left, result)
    #     self.traverse(root.right, result)
