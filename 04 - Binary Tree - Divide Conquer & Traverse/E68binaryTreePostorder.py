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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here

        # method three: do not use recursion
        result = []
        if not root:
            return result

        stack, prevNode = [root], None
        while len(stack) > 0:
            currNode = stack[-1]

            if prevNode is None or prevNode.left == currNode or prevNode.right == currNode:
                if currNode.left is not None:
                    stack.append(currNode.left)
                elif currNode.right is not None:
                    stack.append(currNode.right)
            elif currNode.left == prevNode:
                if currNode.right is not None:
                    stack.append(currNode.right)
            else:
                result.append(currNode.val)
                stack.pop()

            prevNode = currNode

        return result

        # # method two: morris
        # result = []
        # currNode = None

        # while root is not None:
        #     if root.right is not None:
        #         currNode = root.right

        #         while currNode.left is not None and currNode.left != root:
        #             currNode = currNode.left

        #         if currNode.left == root:
        #             currNode.left = None
        #             root = root.left
        #         else:
        #             result.append(root.val)
        #             currNode.left = root
        #             root = root.right
        #     else:
        #         result.append(root.val)
        #         root = root.left

        # # need to reverse
        # result.reverse()

        # return result

    #     # method one: traverse
    #     result = []
    #     self.traverse(root, result)

    #     return result

    # def traverse(self, root, result):
    #     if root is None:
    #         return

    #     self.traverse(root.left, result)
    #     self.traverse(root.right, result)
    #     result.append(root.val)
