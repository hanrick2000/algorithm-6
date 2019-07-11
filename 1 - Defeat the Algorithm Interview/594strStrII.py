
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

        size_source, size_target = len(source), len(target)
        if size_target == 0:
            return size_target

        magic_code = 31
        import random
        base = random.randint(1000000, 2000000)

        power = 1
        for i in range(size_target):
            power = (power * magic_code) % base

        hash_target = 0
        for i in target:
            hash_target = (hash_target * magic_code + ord(i)) % base

        hash_source = 0
        for i in range(size_source):
            hash_source = (hash_source * magic_code + ord(source[i])) % base
            if i < size_target - 1:
                continue

            if i >= size_target:
                # remove the first character to keep the length which is the same the length of the target
                hash_source -= (ord(source[i - size_target]) * power) % base

                if hash_source < 0:
                    hash_source += base

            if hash_source == hash_target:
                # double check
                if source[i - size_target + 1 : i + 1] == target:
                    return i - size_target + 1

        return -1
