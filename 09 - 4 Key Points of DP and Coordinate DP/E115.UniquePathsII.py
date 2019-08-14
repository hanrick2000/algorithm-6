class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        grid = obstacleGrid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    grid[i][j] = 1 - grid[i][j]
                    continue

                if grid[i][j] == 1:
                    grid[i][j] = 0
                elif i == 0:
                    grid[i][j] = grid[i][j - 1]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j]
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[-1][-1]
