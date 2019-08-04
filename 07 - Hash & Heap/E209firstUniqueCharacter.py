class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here

        # method 2:
        # build hash map : character and how often it appears
        counts = collections.Counter(str)

        for char in str:
            if counts[char] == 1:
                return char

        # method 1:
        # counts = {}
        # for char in str:
        #     counts[char] = counts.get(char, 0) + 1

        # for char in str:
        #     if counts[char] == 1:
        #         return char
