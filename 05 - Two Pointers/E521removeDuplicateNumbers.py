class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        count = 0
        if not nums:
            return count

        nums.sort()

        for j in range(1, len(nums)):
            if nums[count] != nums[j]:
                count += 1
                nums[count] = nums[j]

        return count + 1
