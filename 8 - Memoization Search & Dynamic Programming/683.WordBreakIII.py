class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        if not s or not dict:
            return 0

        size, hash = len(s), set()

        for d in dict:
            hash.add(d.lower())

        dp = []
        for i in range(size):
            dp.append([0] * size)
            for j in range(i, size):
                sub = s[i: j + 1].lower()
                if sub in hash:
                    dp[i][j] = 1

        for i in range(size):
            for j in range(i, size):
                for k in range(i, j):
                    dp[i][j] += dp[i][k] * dp[k + 1][j]

        return dp[0][-1]
