"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """
    def convertBST(self, root):
        # write your code here

        # method 2:
        if not root:
            return root

        self.total, stack = 0, []

        node = root
        while node:
            stack.append(node)
            node = node.right

        while stack:
            node = stack[-1]
            self.total += node.val
            node.val = self.total

            if not node.left:
                node = stack.pop()
                while stack and stack[-1].left == node:
                    node = stack.pop()

            else:
                node = node.left
                while node:
                    stack.append(node)
                    node = node.right

        return root

        # method 1:
    #     self.sum = 0
    #     self.helper(root)
    #     return root

    # def helper(self, root):
    #     if not root:
    #         return

    #     if root.right:
    #         self.helper(root.right)

    #     self.sum += root.val
    #     root.val = self.sum

    #     if root.left:
    #         self.helper(root.left)

# leetcode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total, node = 0, root

        while node:
            if not node.right:
                self.total += node.val
                node.val, node = self.total, node.left
            else:
                nextNode = self.get_next(node)
                if not nextNode.left:
                    nextNode.left, node = node, node.right
                else:
                    nextNode.left = None
                    self.total += node.val
                    node.val, node = self.total, node.left

        return root

    def get_next(self, root):
        nextNode = root.right
        while nextNode.left and nextNode.left is not root:
            nextNode = nextNode.left
        return nextNode
