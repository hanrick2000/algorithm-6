class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        size = len(triangle)

        dp = [[0] * size, [0] * size]

        for i in range(size):
            dp[(size - 1) % 2][i] = triangle[size - 1][i]

        for i in range(size - 2, -1, -1):
            for j in range(i + 1):
                dp[i % 2][j] = min(dp[(i + 1) % 2][j], dp[(i + 1) % 2][j + 1]) + triangle[i][j]

        return dp[0][0]
