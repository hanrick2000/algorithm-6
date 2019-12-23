class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        if not nums:
            return nums

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] % 2 == 1:
                l += 1
            elif nums[r] % 2 == 0:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
