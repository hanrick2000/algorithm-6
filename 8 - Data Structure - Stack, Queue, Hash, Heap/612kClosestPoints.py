import heapq

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
        heap = []
        for point in points:
            dist = self.get_distance(point, origin)
            heapq.heappush(heap, (-dist, -point.x, -point.y))

            if len(heap) > k:
                heapq.heappop(heap)

        results = []
        while heap:
            dist, x, y = heapq.heappop(heap)
            results.append(Point(-x, -y))

        results.reverse()
        return results

    def get_distance(self, point, origin):
        # use the ** operator to calculate powers
        return (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2
