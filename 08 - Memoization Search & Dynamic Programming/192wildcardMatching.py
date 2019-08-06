class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        return self.is_match_helper(s, 0, p, 0, {})

    def is_match_helper(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if len(s) == i:
            for index in range(j, len(p)):
                if p[index] != "*":
                    return False
            return True

        if len(p) == j:
            return False

        if p[j] != "*":
            matched = self.is_match_char(s[i], p[j]) and self.is_match_helper(s, i + 1, p, j + 1, memo)
        else:
            matched = self.is_match_helper(s, i + 1, p, j, memo) or self.is_match_helper(s, i, p, j + 1, memo)

        memo[(i, j)] = matched

        return matched

    def is_match_char(self, s, p):
        return s == p or p == "?"
