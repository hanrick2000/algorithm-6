class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        counts = {}
        for char in str:
            counts[char] = counts.get(char, 0) + 1

        for char in str:
            if counts[char] == 1:
                return char
