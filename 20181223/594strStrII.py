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

        target_len = len(target)
        source_len = len(source)

        if target_len == 0:
            return 0

        magic_numb = 31
        import random
        hash_size = random.randint(1000000, 20000000)

        power = 1
        for i in range(target_len):
            power = (power * magic_numb) % hash_size

        target_code = 0
        for i in range(target_len):
            target_code = (target_code * magic_numb + ord(target[i])) % hash_size


        hash_code = 0
        for i in range(source_len):
            hash_code = (hash_code * magic_numb + ord(source[i])) % hash_size
            if i < target_len - 1:
                continue

            if i >= target_len:
                hash_code = (hash_code - ord(source[i - target_len]) * power) % hash_size
                if hash_code < 0:
                    hash_code += hash_size

            if target_code == hash_code:
                # double check
                if source[i - target_len + 1: i + 1] == target:
                    return i - target_len + 1

        return -1
