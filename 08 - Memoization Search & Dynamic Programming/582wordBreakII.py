class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if not s:
            return []

        partitions = []

        for i in range(1, len(s)):
            prefix = s[: i]
            if prefix not in wordDict:
                continue

            sub_partitions = self.dfs(s[i: ], wordDict, memo)
            for sub in sub_partitions:
                partitions.append(prefix + " " + sub)

        if s in wordDict:
            partitions.append(s)

        memo[s] = partitions

        return partitions
