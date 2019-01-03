class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        result = []
        if nums is None or target is None:
            return result

        nums = [(num, i) for i, num in enumerate(nums)]
        nums = sorted(nums, key = lambda x: x[0])
        target = abs(target)

        j, size = 0, len(nums)
        for i in range(size):
            if i == j:
                j += 1

            while j < size and nums[j][0] - nums[i][0] < target:
                j += 1

            if nums[j][0] - nums[i][0] == target:
                result.append(nums[i][1] + 1)
                result.append(nums[j][1] + 1)
                break

        if result[0] > result[1]:
            result[0], result[1] = result[1], result[0]

        return result
