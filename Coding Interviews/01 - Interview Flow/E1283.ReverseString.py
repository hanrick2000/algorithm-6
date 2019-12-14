class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseString(self, s):
        # write your code here
        size = len(s)
        for i in range(size // 2):
            s[i], s[size - i - 1] = s[size - i - 1], s[i]

        return s
