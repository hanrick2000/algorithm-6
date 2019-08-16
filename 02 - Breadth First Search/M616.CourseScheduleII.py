class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        if not prerequisites:
            return [num for num in range(numCourses)]

        courses, edges, degree = [], {num: [] for num in range(numCourses)}, [0] * numCourses
        for i, j in prerequisites:
            edges[j].append(i)
            degree[i] += 1

        queue = collections.deque([num for num in range(numCourses) if degree[num] == 0])
        while queue:
            prerequisite = queue.popleft()
            courses.append(prerequisite)

            for course in edges[prerequisite]:
                degree[course] -= 1
                if degree[course] == 0:
                    queue.append(course)

        if len(courses) == numCourses:
            return courses

        return []
