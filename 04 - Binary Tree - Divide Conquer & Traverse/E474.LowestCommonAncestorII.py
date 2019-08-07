"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        parents = {}

        while A is not root:
            parents[A] = 1
            A = A.parent

        while B is not root:
            if B in parents:
                return B

            #parents[B] = 1 # isn't necessary
            B = B.parent

        return root
