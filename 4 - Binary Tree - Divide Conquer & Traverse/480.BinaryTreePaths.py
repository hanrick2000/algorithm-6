"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here

        # # method 1: DFS of the Divider Conquer
        # if root is None:
        #     return []
        #
        # if root.left is None and root.right is None:
        #     return [str(root.val)]
        #
        # results = []
        # for path in self.binaryTreePaths(root.left):
        #     results.append(str(root.val) + "->" + path)
        #
        # for path in self.binaryTreePaths(root.right):
        #     results.append(str(root.val) + "->" + path)
        #
        # return results

        # method 2: Traversal
        if root is None:
            return []

        results = []
        self.dfs(root, [str(root.val)], results)

        return results

    def dfs(self, root, path, results):
        if root.left is None and root.right is None:
            results.append("->".join(path))

        if root.left:
            path.append(str(root.left.val))
            self.dfs(root.left, path, results)
            path.pop()

        if root.right:
            path.append(str(root.right.val))
            self.dfs(root.right, path, results)
            path.pop()
