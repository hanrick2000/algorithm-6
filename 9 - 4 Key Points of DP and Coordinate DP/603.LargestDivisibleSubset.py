class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        dp, father, maxLen, maxIndex = [], [], 0, -1

        nums.sort();
        for i in range(len(nums)):
            dp.append(1)
            father.append(-1)
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1 + dp[j] > dp[i]:
                    dp[i] = dp[j] + 1
                    father[i] = j

            if dp[i] > maxLen:
                maxLen = dp[i]
                maxIndex = i

        result = []
        for i in range(maxLen):
            result.append(nums[maxIndex])
            maxIndex = father[maxIndex]

        return result
