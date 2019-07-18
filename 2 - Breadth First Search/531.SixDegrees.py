"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        # write your code here
        connected, queue = {}, collections.deque([s])
        connected[s] = 0

        while queue:
            node = queue.popleft()
            if node == t:
                return connected[node]

            for neighbor in node.neighbors:
                if neighbor not in connected:
                    connected[neighbor] = connected[node] + 1
                    queue.append(neighbor)

        return -1
