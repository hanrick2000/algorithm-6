class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if not nums:
            return nums

        # use two Points, both from left to right.
        # keep the date on the left side stablely
        i = -1
        for j in range(len(nums)):
            if nums[j] != 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
