class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums)

        while left + 1 < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle
            else:
                right = middle

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right

        return -1
