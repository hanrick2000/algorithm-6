class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        
        # method 2:
        path = [1 for _ in range(n)]

        for _ in range(1, m):
            for i in range(1, n):
                path[i] += path[i - 1]

        return path[-1]

        # method 1:
        # grid = []
        # for i in range(m):
        #     grid.append([]);
        #     for j in range(n):
        #         if i == 0 or j == 0:
        #             grid[i].append(1)
        #         else:
        #             grid[i].append(grid[i - 1][j] + grid[i][j - 1])

        # return grid[-1][-1]
