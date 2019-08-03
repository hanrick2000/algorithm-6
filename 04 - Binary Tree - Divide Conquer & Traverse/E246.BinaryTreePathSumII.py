"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        result = []
        if not root:
            return result

        self.dfs(root, target, 0, [], result)

        return result

    def dfs(self, root, target, level, path, result):
        if root is None:
            return

        path.append(root.val)
        sum = target
        for i in range(level, -1, -1):
            sum -= path[i]
            if not sum:
                result.append(path[i:])

        self.dfs(root.left, target, level + 1, path, result)
        self.dfs(root.right, target, level + 1, path, result)

        path.pop()
