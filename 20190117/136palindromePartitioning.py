class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        results = []

        self.dfs(s, [], results)

        return results

    def dfs(self, s, subset, results):
        if not s:
            results.append(list(subset))
            return

        for i in range(1, len(s) + 1):
            prefix = s[: i]
            if self.is_palindrome(prefix):
                subset.append(prefix)
                self.dfs(s[i: ], subset, results)
                subset.pop()

    def is_palindrome(self, s):
        return s == s[::-1]
