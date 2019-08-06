class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here

        words = teststr.split()

        words_size, hashmap = len(words), {}
        if words_size != len(pattern): return False

        for i, word in enumerate(words):
            if pattern[i] not in hashmap:
                hashmap[pattern[i]] = word
            elif hashmap[pattern[i]] != word:
                return False

        # make sure the keys count is equal to the values count
        if len(hashmap) != len(set(hashmap.values())): return False

        return True
