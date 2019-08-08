class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here
        dp = [0]
        for i in range(1, amount + 1):
            dp.append(sys.maxsize)
            for coin in coins:
                if i < coin or dp[i - coin] == sys.maxsize:
                    continue

                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != sys.maxsize else -1
