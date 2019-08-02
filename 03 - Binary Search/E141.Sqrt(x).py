class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x < 0:
            return 0

        # write your code here
        left, right = 0, x if x < 2 else x // 2
        while left + 1 < right:
            mid = left + (right - left) // 2
            squre = mid * mid
            if squre == x:
                return mid
            elif squre < x:
                left = mid
            else:
                right = mid

        if right * right <= x:
            return right

        return left
