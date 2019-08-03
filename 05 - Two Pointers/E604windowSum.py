class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        size = len(nums)
        if not nums or k < 2:
            return nums

        # method 2
        if size < k:
            return []

        result = [0]
        for i in range(k):
            result[0] += nums[i]

        for i in range(1, size - k + 1):
            result.append(0)
            result[i] += (result[i - 1] - nums[i - 1] + nums[i + k - 1])

        return result

        # # method 1
        # left, result = 0, []
        #
        # while left + k <= size:
        #     # Here is the most important part, only the first k numbers need to be added together
        #     if left == 0:
        #         sum = 0
        #         for i in range(k):
        #             sum += nums[left + i]
        #     else:
        #         sum -= nums[left - 1] - nums[left + k - 1]
        #     result.append(sum)
        #
        #     left += 1
        #
        # return result
