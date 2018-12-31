class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        result, base = 1, x

        # negative n become positive n
        if n < 0:
            base = 1 / base
            n *= -1

        while n != 0:
            if n % 2 == 1:
                result *= base
            base *= base
            n //= 2
        return result
