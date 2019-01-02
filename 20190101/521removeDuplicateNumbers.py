class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        result = 0
        if nums is None or len(nums) == 0:
            return result

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                result += 1
                # Adding this judgment saves time
                if result != i:
                    nums[result] = nums[i]

        result += 1

        return result
