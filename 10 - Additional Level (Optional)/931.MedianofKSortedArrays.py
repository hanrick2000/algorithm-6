class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        # write your code here
        result = 0.0
        if not nums:
            return result

        size = sum(len(array) for array in nums)
        if size == 0:
            return result

        if size % 2 == 1:
            return self.find_kth(nums, size // 2 + 1) * 1.0

        return (self.find_kth(nums, size // 2) + self.find_kth(nums, size // 2 + 1)) / 2.0

    def find_kth(self, nums, k):
        start, end = self.get_range(nums)

        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_smaller_or_equal(nums, mid) >= k:
                end = mid
            else:
                start = mid
        if self.get_smaller_or_equal(nums, start) >= k:
            return start
        return end


    def get_range(self, nums):
        return min(num[0] for num in nums if len(num)), max(num[-1] for num in nums if len(num))

    def get_smaller_or_equal(self, nums, value):
        count = 0
        for num in nums:
            count += self.get_smaller_or_equal_in_num(num, value)
        return count

    def get_smaller_or_equal_in_num(self, num, value):
        if not num:
            return 0

        start, end = 0, len(num) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if num[mid] > value:
                end = mid
            else:
                start = mid

        if num[start] > value:
            return start
        if num[end] > value:
            return end

        return end + 1
