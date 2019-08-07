class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here

        # f(0) = 1, f(1) = 1, f(2) = 2, f(n) = f(n - 1) + f(n - 2) + f(n - 3)
        first, second, third = 1, 1, 2
        if n < 2: return first

        for i in range(3, n + 1):
            first, second, third = second, third, first + second + third

        return third
