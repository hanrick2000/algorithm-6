class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def countPrimes(self, n):
        # write your code here
        if n < 3:
            return 0

        result, hash = 0, [True] * n
        for num in range(2, n):
            if not hash[num]:
                continue

            result += 1
            for j in range(num * num, n, num):
                hash[j] = False

        return result
