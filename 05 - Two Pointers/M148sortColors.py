class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return

        redIndex, blueIndex, index = 0, len(nums) - 1, 0

        while index <= blueIndex:
            if nums[index] == 0:
                self.swap(nums, index, redIndex)
                redIndex += 1
                index += 1
            elif nums[index] == 2:
                self.swap(nums, index, blueIndex)
                blueIndex -= 1
            else:
                index += 1

    def swap(self, nums, first, second):
        if first != second:
            nums[first], nums[second] = nums[second], nums[first]
