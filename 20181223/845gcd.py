class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        # write your code here
        if (a > b):
            big = a
            small = b
        else:
            big = b
            small = a

        if small != 0:
            return self.gcd(small, big % small)
        else:
            return big
