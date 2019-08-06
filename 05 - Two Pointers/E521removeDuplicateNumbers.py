class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        count = 0
        if nums is None or len(nums) == 0:
            return count

        nums.sort()

        for j in range(1, len(nums)):
            if nums[j - 1] != nums[j]:
                count += 1
                nums[count] = nums[j]

        # # method one
        # for i in range(1, len(nums)):
        #     if nums[i - 1] != nums[i]:
        #         count += 1
        #         if count != i:
        #             nums[count] = nums[i]

        count += 1

        return count
