class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        results = []

        s = list(str)
        s.sort()
        next = True

        while next:
            results.append(''.join(s))
            next = self.dfs(s)

        return results

    def dfs(self, source):
        size = len(source)

        i = size - 1
        while i > 0 and source[i] <= source[i - 1]:
            i -= 1

        if i <= 0:
            return False

        j = size - 1
        while source[j] <= source[i - 1]:
            j -= 1

        self.swapItem(source, j, i - 1)

        self.swapList(source, i, size - 1)

        return True

    def swapItem(self, nums, i, j):
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]

    def swapList(self, nums, i, j):
        while i < j:
            self.swapItem(nums, i, j)
            i += 1
            j -= 1
