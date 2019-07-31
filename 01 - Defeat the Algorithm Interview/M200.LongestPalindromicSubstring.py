class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        result = ""
        if not s:
            return result

        for i in range(len(s)):
            sub = self.find_palindrome(s, i, i)
            if len(sub) > len(result):
                result = sub
            sub = self.find_palindrome(s, i, i + 1)
            if len(sub) > len(result):
                result = sub

        return result

    def find_palindrome(self, s, left, right):
        size = len(s)
        while left >= 0 and right < size and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]
