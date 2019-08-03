class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        size = len(nums)
        if nums is None or k < 2:
            return nums

        left, result = 0, []

        while left + k <= size:
            # Here is the most important part, only the first k numbers need to be added together
            if left == 0:
                sum = 0
                for i in range(k):
                    sum += nums[left + i]
            else:
                sum -= nums[left - 1] - nums[left + k - 1]
            result.append(sum)

            left += 1

        return result
