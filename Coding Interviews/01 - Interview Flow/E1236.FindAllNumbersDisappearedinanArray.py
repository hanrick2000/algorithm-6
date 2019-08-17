class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def findDisappearedNumbers(self, nums):
        # write your code here
        # method 2:
        if not nums:
            return nums

        size = len(nums)
        for i in range(size):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1

        result = []
        for i in range(size):
            if nums[i] > 0:
                result.append(i + 1)

        return result

        # method 1:
        # s = set(nums)
        # return [num for num in range(1, len(nums) + 1) if num not in s]


# leetcode
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1, len(nums)+1)).difference(set(nums))
