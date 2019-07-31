class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        if not len(grid) or not len(grid[0]):
            return 0

        row_size, col_size, queue = len(grid), len(grid[0]), collections.deque()

        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == 1:
                    queue.append((i, j))

        day, direction = 0, [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            size = len(queue)
            day += 1
            for n in range(size):
                (i, j) = queue.popleft()
                for (di, dj) in direction:
                    next_i, next_j = i + di, j + dj
                    if next_i < 0 or next_i >= row_size or next_j < 0 or next_j >= col_size:
                        continue
                    if grid[next_i][next_j] > 0:
                        continue

                    grid[next_i][next_j] = 1
                    queue.append((next_i, next_j))

        for i in range(row_size):
            for j in range(col_size):
                if not grid[i][j]:
                    return -1

        return day - 1
