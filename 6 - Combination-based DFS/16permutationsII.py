class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        results = []
        if nums is None:
            return results

        nums.sort()
        self.dfs(nums, [False for _ in nums], [], results)

        return results

    def dfs(self, nums, visited, permutation, results):
        if len(nums) == len(permutation):
            results.append(list(permutation))
            return

        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                continue

            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, permutation, results)

            visited[i] = False
            permutation.pop()
        
