class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        edges, degrees = {i: [] for i in range(numCourses)}, [0] * numCourses
        for i, j in prerequisites:
            edges[j].append(i)
            # out-degree
            degrees[i] += 1

        queue, n = collections.deque([]), 0

        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            n += 1

            for i in edges[node]:
                degrees[i] -= 1
                if degrees[i] == 0:
                    queue.append(i)

        return n == numCourses
