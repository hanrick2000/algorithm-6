class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        results = []
        if nums is None:
            return results

        nums.sort()
        self.dfs(nums, 0, [], results)

        return  results

    def dfs(self, nums, startIndex, subset, results):
        results.append(list(subset))

        for i in range(startIndex, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and i > startIndex:
                continue

            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            subset.pop()
