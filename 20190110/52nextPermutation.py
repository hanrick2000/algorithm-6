class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        if not nums:
            return nums

        # find i when nums[i] > nums[i - 1] or i is 0
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i != 0:
            j = len(nums) - 1
            # find j when nums[j] > nums[i - 1]
            while nums[j] <= nums[i - 1]:
                j -= 1
            # swap two items
            self.swapItem(nums, j, i - 1)

        # swap from i to the end of the list
        self.swapList(nums, i, len(nums) - 1)

        return nums

    def swapItem(self, nums, i, j):
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]

    def swapList(self, nums, i, j):
        while i < j:
            self.swapItem(nums, i, j)
            i += 1
            j -= 1
