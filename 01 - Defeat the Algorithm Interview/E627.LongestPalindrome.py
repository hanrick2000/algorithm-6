class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here

        # method 1
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

        # # method 2
        # hash, l, r = set(), 0, len(s) - 1
        # while l <= r:
        #     if s[l] in hash:
        #         hash.remove(s[l])
        #     else:
        #         hash.add(s[l])

        #     if r != l:
        #         if s[r] in hash:
        #             hash.remove(s[r])
        #         else:
        #             hash.add(s[r])

        #     l += 1
        #     r -= 1

        # hash_size = len(hash)
        # if hash_size:
        #     hash_size -= 1

        # return len(s) - hash_size

        # # method 3
        # hash = set()
        #
        # for char in s:
        #     if char in hash:
        #         hash.remove(char)
        #     else:
        #         hash.add(char)
        #
        # hash_size = len(hash)
        # if hash_size:
        #     hash_size -= 1
        #
        # return len(s) - hash_size
