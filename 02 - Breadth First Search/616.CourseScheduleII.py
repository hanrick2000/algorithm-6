class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        edges, degrees = {i: [] for i in range(numCourses)}, [0] * numCourses

        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1

        result, queue = [], collections.deque([])
        for i in range(numCourses):
            if not degrees[i]:
                queue.append(i)

        while queue:
            node = queue.popleft()
            result.append(node)

            for i in edges[node]:
                degrees[i] -= 1
                if not degrees[i]:
                    queue.append(i)

        if len(result) == numCourses:
            return result

        return []
