"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    def __init__(self):
        self.dict = {}

    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return None

        if node.label in self.dict:
            return self.dict[node.label]

        root = UndirectedGraphNode(node.label)
        self.dict[node.label] = root

        for neighbor in node.neighbors:
            root.neighbors.append(self.cloneGraph(neighbor))

        return root
