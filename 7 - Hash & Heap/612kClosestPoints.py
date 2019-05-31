# method 2 is slow, need to check again

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        if not points:
            return points

        self.origin = origin
        self.heapify(points)

        results = []
        for i in range(k):
            results.append(self.pop(points))

        return results

    def heapify(self, points):
        for i in range(len(points) // 2, -1, -1):
            self.shift_down(points, i)

    def shift_down(self, points, index):
        size = len(points)
        while index < size:
            left = index * 2 + 1
            right, minIndex = left + 1, index

            if left < size and self.compare(points[minIndex], points[left]) > 0:
                minIndex = left
            if right < size and self.compare(points[minIndex], points[right]) > 0:
                minIndex = right
            if minIndex == index:
                break

            points[index], points[minIndex] = points[minIndex], points[index]
            index = minIndex

    def pop(self, points):
        top = points[0]
        points[0] = points[len(points) - 1]
        self.shift_down(points, 0)

        return top

    def compare(self, pointA, pointB):
        dist = self.get_distance(pointA, self.origin) - self.get_distance(pointB, self.origin)
        if dist != 0:
            return dist

        if pointA.x != pointB.x:
            return pointA.x - pointB.x

        return pointA.y - pointB.y

    def get_distance(self, point, origin):
        # use the ** operator to calculate powers
        return (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2

# # method 1
# import heapq

# """
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
# """

# class Solution:
#     """
#     @param points: a list of points
#     @param origin: a point
#     @param k: An integer
#     @return: the k closest points
#     """
#     def kClosest(self, points, origin, k):
#         # write your code here
#         heap = []
#         for point in points:
#             dist = self.get_distance(point, origin)
#             heapq.heappush(heap, (-dist, -point.x, -point.y))

#             if len(heap) > k:
#                 heapq.heappop(heap)

#         results = []
#         while heap:
#             dist, x, y = heapq.heappop(heap)
#             results.append(Point(-x, -y))

#         results.reverse()
#         return results

#     def get_distance(self, point, origin):
#         # use the ** operator to calculate powers
#         return (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2
