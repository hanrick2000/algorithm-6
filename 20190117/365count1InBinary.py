class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here

        # method 3
        count, mask = 0, 2 ** 32 - 1
        num &= mask

        while num:
            num &= num - 1
            count += 1

        return count

        # method 2
        # count, bound = 0, 2**32 - 1

        # while num != 0 and num > -bound:
        #     num &= num - 1
        #     count += 1

        # return count

        # # method 1
        # count = 0

        # for i in range(32):
        #     count += num & 1
        #     num >>= 1

        # return count
