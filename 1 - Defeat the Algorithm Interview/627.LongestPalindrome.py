class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        hash = {}

        for char in s:
            if char in hash:
                del hash[char]
            else:
                hash[char] = 1

        hash_size = len(hash)
        if hash_size > 0:
            hash_size -= 1

        return len(s) - hash_size
