class Solution:
    """
    @param graph: a list of Undirected graph node
    @param A: nodeA
    @param B: nodeB
    @return:  the length of the shortest path
    """
    def shortestPath(self, graph, A, B):
        # Write your code here
        if A == B:
            return 1

        # Bidirectional BFS
        startQueue, endQueue, step = collections.deque([A]), collections.deque([B]), 0
        visted = set([A, B])

        while startQueue and endQueue:
            startSize, endSize = len(startQueue), len(endQueue)

            step += 1
            for _ in range(startSize):
                node = startQueue.popleft()
                for neighbor in node.neighbors:
                    if neighbor in endQueue:
                        return step

                    if neighbor not in visted:
                        visted.add(neighbor)
                        startQueue.append(neighbor)

            step += 1
            for _ in range(endSize):
                node = endQueue.popleft()
                for neighbor in node.neighbors:
                    if neighbor in startQueue:
                        return step

                    if neighbor not in visted:
                        visted.add(neighbor)
                        endQueue.append(neighbor)

        return -1
