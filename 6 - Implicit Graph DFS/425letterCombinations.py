class Solution:
    def __init__(self):
        self.KEYBOARD = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }

    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        results = []

        if not digits:
            return results

        self.dfs(digits, 0, '', results)

        return results

    def dfs(self, digits, start, substring, results):
        if start == len(digits):
            results.append(substring)
            return

        for letter in self.KEYBOARD[digits[start]]:
            self.dfs(digits, start + 1, substring + letter, results)
