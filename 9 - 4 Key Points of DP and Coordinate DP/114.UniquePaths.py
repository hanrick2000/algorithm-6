class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        grid = []
        for i in range(m):
            grid.append([]);
            for j in range(n):
                if i == 0 or j == 0:
                    grid[i].append(1)
                else:
                    grid[i].append(grid[i - 1][j] + grid[i][j - 1])

        return grid[-1][-1]
