class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here

        # method 2
        result = []
        if nums is None:
            return result

        nums.sort()
        self.dfs(nums, 0, [], result)

        return result

    def dfs(self, nums, startIndex, subset, result):
        result.append(list(subset))

        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, result)
            subset.pop()

    #     # method 1
    #     self.result = []
    #     self.search(sorted(nums), [], 0)

    #     return self.result

    # def search(self, nums, subset, index):
    #     if index == len(nums):
    #         self.result.append(list(subset))
    #         return

    #     subset.append(nums[index])
    #     self.search(nums, subset, index + 1)
    #     # Backtracking
    #     subset.pop()
    #     self.search(nums, subset, index + 1)
