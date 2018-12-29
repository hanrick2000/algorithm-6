class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if nums is None:
            return -1

        count = len(nums)
        for i in range(count - 1):
            if nums[i] > nums[i + 1]:
                # three steps to revverse
                self.reverse(nums, 0, i)
                self.reverse(nums, i + 1, count - 1)
                self.reverse(nums, 0, count - 1)
                return 0

    def reverse(self, nums, start, end):
        left, right = start, end
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
