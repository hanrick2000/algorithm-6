class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        # write your code here
        if not nums:
            return

        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i != 0:
            j = len(nums) - 1
            while nums[j] <= nums[i - 1]:
                j -= 1

            self.swapItem(nums, j, i - 1)

        self.swapList(nums, i, len(nums) - 1)

    def swapItem(self, nums, i, j):
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]

    def swapList(self, nums, i, j):
        while i < j:
            self.swapItem(nums, i, j)
            i += 1
            j -= 1
