class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        size = len(s)
        # if size == 0 then return 0
        if not size:
            return size

        dp = [[0] * size for _ in range(size)]
        for i in range(size - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][size - 1]
