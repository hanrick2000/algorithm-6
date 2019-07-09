from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        result, visited, size_item = 0, set(), len(grid[0])

        for i in range(len(grid)):
            for j in range(size_item):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    result += 1

        return result

    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))

        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x, next_y = x + delta_x, y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue

                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])

        return 0 <= x < n and 0 <= y < m and (x, y) not in visited and grid[x][y]
