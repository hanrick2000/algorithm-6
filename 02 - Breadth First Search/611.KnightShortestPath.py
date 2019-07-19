"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        row_size, col_size = len(grid), len(grid[0])

        record = [[sys.maxsize] * col_size for _ in range(row_size)]
        record[source.x][source.y] = 0

        queue = collections.deque([source])
        dist = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

        while queue:
            node = queue.popleft()
            for dx, dy in dist:
                x, y = dx + node.x, dy + node.y

                if x >= 0 and x < row_size and y >= 0 and y < col_size and \
                   not grid[x][y] and record[node.x][node.y] + 1 < record[x][y]:
                       record[x][y] = record[node.x][node.y] + 1
                       queue.append(Point(x, y))

        if record[destination.x][destination.y] == sys.maxsize:
            return -1

        return record[destination.x][destination.y]
