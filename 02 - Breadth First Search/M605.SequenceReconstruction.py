class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        graph = self.build_graph(seqs)
        result = self.sort_topological(graph)

        return result == org

    def build_graph(self, seqs):
        # initialize a graph
        graph = {}

        for seq in seqs:
            for i in seq:
                if i not in graph:
                    graph[i] = set()

        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph

    def sort_topological(self, graph):
        indegrees, queue = self.get_indegrees(graph), []

        for node in graph:
            if not indegrees[node]:
                queue.append(node)

        result = []
        while queue:
            # need only one sequence
            if len(queue) > 1:
                return None

            node = queue.pop()
            result.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if not indegrees[neighbor]:
                    queue.append(neighbor)

        if len(result) == len(graph):
            return result

        return None

    def get_indegrees(self, graph):
        indegrees = {node: 0 for node in graph}

        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1

        return indegrees
