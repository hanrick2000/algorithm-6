class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        result = []

        import math
        up = math.sqrt(num)

        for i in range(2, int(up + 1)):
            while num % i == 0:
                num //= i
                result.append(i)

            if num <= 1:
                break

        if num > 1:
            result.append(num)

        return result
