class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here

        results = []
        if not candidates:
            return results

        candidates.sort()
        self.dfs(candidates, 0, [], target, results)

        return results

    def dfs(self, nums, start, combination, target, results):
        if target == 0:
            results.append(list(combination))
            return

        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i - 1]:
                continue

            if target < nums[i]:
                break

            combination.append(nums[i])
            self.dfs(nums, i, combination, target - nums[i], results)
            combination.pop()
