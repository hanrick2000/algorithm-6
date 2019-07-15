class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if source is None or target is None:
            return -1

        s_len, t_len = len(source), len(target)
        for i in range(s_len - t_len + 1):
            j = 0
            while j < t_len:
                if source[i + j] != target[j]:
                    break
                j += 1

            if j == t_len:
                return i

        return -1
