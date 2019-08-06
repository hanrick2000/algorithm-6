class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here

        height = [a[1] for a in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
        dp, size = [0] * len(height), 0

        import bisect
        for h in height:
            i = bisect.bisect_left(dp, h, 0, size)
            dp[i] = h
            if i == size:
                size += 1
        return size
