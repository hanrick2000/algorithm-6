class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        results = []

        self.dfs(n + 1, 1, [], k, results)

        return results

    def dfs(self, n, start, combination, k, results):
        if k == 0:
            results.append(list(combination))
            return

        for i in range(start, n):
            combination.append(i)
            self.dfs(n, i + 1, combination, k - 1, results)
            combination.pop()
