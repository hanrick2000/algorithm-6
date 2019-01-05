"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        indegrees = self.getIndegrees(graph)

        result = []
        startNodes = [node for node in graph if indegrees[node] == 0]
        queue = collections.deque(startNodes)

        # BFS
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return result

    """
        return the indegree of nodes
    """
    def getIndegrees(self, graph):
        indegrees = {node: 0 for node in graph}

        for node in graph:
            for neighbor in node.neighbors:
                indegrees[neighbor] += 1

        return indegrees
