class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here

        # method two: iteration
        results = []

        nums.sort()
        next = True

        while next:
            current = [num for num in nums]
            results.append(current)

            next = self.nextPermutation(nums)

        return results

    def nextPermutation(self, nums):
        size = len(nums)
        i = size - 1

        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i <= 0:
            return False

        j = size - 1

        while nums[j] <= nums[i - 1]:
            j -= 1

        self.swapItem(nums, j, i - 1)

        self.swapList(nums, i, size - 1)

        return True

    def swapItem(self, nums, i, j):
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]

    def swapList(self, nums, i, j):
        while i < j:
            self.swapItem(nums, i, j)
            i += 1
            j -= 1

    #     # method one: recursion
    #     results = []
    #     if nums is None:
    #         return results

    #     self.dfs(nums, [False for _ in nums], [], results)

    #     return results

    # def dfs(self, nums, visited, permutation, results):
    #     if len(nums) == len(permutation):
    #         results.append(list(permutation))
    #         return

    #     for i in range(len(nums)):
    #         if visited[i]:
    #             continue

    #         permutation.append(nums[i])
    #         visited[i] = True
    #         self.dfs(nums, visited, permutation, results)

    #         visited[i] = False
    #         permutation.pop()
