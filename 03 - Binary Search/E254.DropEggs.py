class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def dropEggs(self, n):
        # write your code here
        # method 2
        result = int(math.sqrt(n * 2))

        while result * (result + 1) // 2 < n:
            result += 1

        return result

        # method 1
        # result, sum = 0, 0
        # while sum < n:
        #     result += 1
        #     sum += result

        # return result
        
