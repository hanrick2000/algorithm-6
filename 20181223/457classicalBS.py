class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if nums is None or target is None:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] < target:
                left = middle
            else:
                right = middle

        if nums[left] == target:
            return left

        if nums[right] == target:
            return right

        return -1
