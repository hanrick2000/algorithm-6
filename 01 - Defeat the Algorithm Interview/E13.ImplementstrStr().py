class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here

        # method 2:
        # if source is None or target is None:
        #     return -1

        # size_s, size_t = len(source), len(target)
        # if not size_t:
        #     return 0

        # magic_code, base, power, hash_t = 31, 100000001, 1, 0
        # for i in range(size_t):
        #     power = (power * magic_code) % base
        #     hash_t = (hash_t * magic_code + ord(target[i])) % base

        # hash_s = 0
        # for i in range(size_s):
        #     hash_s = (hash_s * magic_code + ord(source[i])) % base
        #     if i < size_t - 1:
        #         continue

        #     if i >= size_t:
        #         hash_s -= (ord(source[i - size_t]) * power) % base

        #         if hash_s < 0:
        #             hash_s += base

        #     if hash_s == hash_t:
        #         return i - size_t + 1

        # return -1

        # method 1:
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
