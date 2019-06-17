class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        self.size = len(nums)
        self.bit = [0] * (self.size + 1)
        for i in range(self.size):
            self.add(i, self.array[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.add(i, val - self.array[i])
        self.array[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j) - self.sum(i - 1)

    def add(self, i, val):
        i += 1
        while i <= self.size:
            self.bit[i] += val
            i += self.lowbit(i)

    def lowbit(self, val):
        return val & (-val)

    def sum(self, i):
        i += 1
        result = 0
        while i > 0:
            result += self.bit[i]
            i -= self.lowbit(i)

        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
