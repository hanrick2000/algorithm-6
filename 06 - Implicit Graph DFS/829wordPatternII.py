class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        return self.is_match(pattern, str, {}, set())

    def is_match(self, p, s, hashMap, used):
        if not p:
            return not s

        char = p[0]
        if char in hashMap:
            word = hashMap[char]
            if not s.startswith(word):
                return False
            return self.is_match(p[1: ], s[len(word): ], hashMap, used)

        for i in range(len(s)):
            word = s[: i + 1]
            if word in used:
                continue

            used.add(word)
            hashMap[char] = word

            if self.is_match(p[1: ], s[i + 1: ], hashMap, used):
                return True

            del hashMap[char]
            used.remove(word)

        return False
