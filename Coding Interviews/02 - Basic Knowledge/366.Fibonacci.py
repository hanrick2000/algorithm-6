class Solution:
    def __init__(self):
        self.nums = [0, 1]

    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n < 1:
            return 0

        for i in range(len(self.nums), n):
            self.nums.append(self.nums[i - 2] + self.nums[i - 1])

        return self.nums[n - 1]
