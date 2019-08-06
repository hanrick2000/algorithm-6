class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        return self.is_match_helper(s, 0, p, 0, {})

    def is_match_helper(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if len(s) == i:
            return self.is_pattern_empty(p, j)

        if len(p) == j:
            return False

        if j + 1 < len(p) and p[j + 1] == "*":
            matched = self.is_match_char(s[i], p[j]) and self.is_match_helper(s, i + 1, p, j, memo) or self.is_match_helper(s, i, p, j + 2, memo)
        else:
            matched = self.is_match_char(s[i], p[j]) and self.is_match_helper(s, i + 1, p, j + 1, memo)

        memo[(i, j)] = matched
        return matched

    def is_pattern_empty(self, p, start):
        size = len(p)
        for i in range(start, size, 2):
            if i + 1 >= size or p[i + 1] != "*":
                    return False
        return True

    def is_match_char(self, s, p):
        return s == p or p == "."
