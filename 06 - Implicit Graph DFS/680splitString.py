class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here

        # method 2
        results = []

        self.dfs(s, [], results)

        return results

    def dfs(self, s, subset, results):
        if not s:
            results.append(list(subset))
            return

        for i in range(2):
            if i + 1 <= len(s):
                subset.append(s[: i + 1])
                self.dfs(s[i + 1:], subset, results)
                subset.pop()

    #     # method 1
    #     results = []

    #     self.dfs(s, 0, [], results)

    #     return results

    # def dfs(self, s, start, subset, results):
    #     if s is None or start == len(s):
    #         results.append(subset)
    #         return

    #     self.dfs(s, start + 1, subset + [s[start]], results)

    #     if start + 2 <= len(s):
    #         subset.append(s[start: (start + 2)])
    #         self.dfs(s, start + 2, subset, results)
