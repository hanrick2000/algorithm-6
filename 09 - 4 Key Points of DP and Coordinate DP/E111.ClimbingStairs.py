class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here

        #  Fibonacci Number
        if n <= 0: return 0

        step = [1, 1]

        for i in range(n - 1):
            step.append(step[-2] + step[-1])

        return step[n]

# leetcode
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first, second = 1, 2
        for i in range(3, n + 1):
            first, second = second, first + second

        return second
