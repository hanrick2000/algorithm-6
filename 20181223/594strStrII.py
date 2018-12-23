class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        # write your code here

        if source is None or target is None:
            return -1

        if target == "":
            return 0

        seed = 31
        hash_size = 1000000
        target_len = len(target)

        power = 1
        for i in range(target_len):
            power = (power * seed) % hash_size

        target_code = 0
        for i in range(target_len):
            target_code = (target_code * seed + ord(target[i])) % hash_size

        hash_len = len(source)
        hash_code = 0
        for i in range(hash_len):
            hash_code = (hash_code * seed + ord(source[i])) % hash_size
            if i < target_len - 1:
                continue

            if i >= target_len:
                hash_code = (hash_code - ord(source[i - target_len]) * power) % hash_size
                if hash_code < 0:
                    hash_code += hash_size

            if target_code == hash_code:
                if source[i - target_len + 1: i + 1] == target:
                    return i - target_len + 1

        return -1
