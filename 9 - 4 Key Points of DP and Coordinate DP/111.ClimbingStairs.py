class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n <= 0: return 0

        step = [1, 1]

        for i in range(n - 1):
            step.append(step[-2] + step[-1])

        return step[n]
