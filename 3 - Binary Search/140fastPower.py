class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b

        result = self.fastPower(a, b, n // 2)
        result *= result
        result %= b

        if n % 2 == 1:
            result *= a
            result %= b

        return result

        # result, base = 1, a
        #
        # while n > 0:
        #     if n % 2 == 1:
        #         result *= base
        #         result %= b
        #     base *= base
        #     base %= b
        #     n //= 2
        #
        # result %= b
        # return result


    #     power = self.power(a, n)
    #     return power % b

    # def power(self, a, n):
    #     result = 1

    #     if n == 0:
    #         return result

    #     print(n, result)
    #     result = self.power(a, n // 2)
    #     result *= result

    #     if n % 2 == 1:
    #         result *= a

    #     return result
