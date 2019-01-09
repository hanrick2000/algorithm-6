class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        self.result = []
        self.search(sorted(nums), [], 0)

        return self.result

    def search(self, nums, subset, index):
        if index == len(nums):
            self.result.append(list(subset))
            return

        subset.append(nums[index])
        self.search(nums, subset, index + 1)
        # Backtracking
        subset.pop()
        self.search(nums, subset, index + 1)
