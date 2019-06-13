class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        prefix_sum = 0

        if not nums:
            return prefix_sum

        max_sum, min_sum = -sys.maxsize, 0

        for num in nums:
            prefix_sum += num

            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum
