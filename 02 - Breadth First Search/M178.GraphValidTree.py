class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n - 1 != len(edges):
            return False

        neighbors, visited, queue = {}, {0: True}, collections.deque([0])
        for i, j in edges:
            if i not in neighbors:
                neighbors[i] = []
            neighbors[i].append(j)

            if j not in neighbors:
                neighbors[j] = []
            neighbors[j].append(i)

        while queue:
            node = queue.popleft()
            visited[node] = True
            if node not in neighbors:
                continue

            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return len(visited) == n
