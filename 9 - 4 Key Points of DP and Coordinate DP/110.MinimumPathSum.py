class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i > 0 or j > 0:
                    if i == 0:
                        grid[i][j] += grid[i][j - 1]
                    elif j == 0:
                        grid[i][j] += grid[i - 1][j]
                    else:
                        grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])

        return grid[-1][-1]
