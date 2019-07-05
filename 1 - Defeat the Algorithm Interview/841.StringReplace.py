class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):
        # Write your code here
        seed, mod, maxLen = 31, 1000000007, -1
        result = 0
        aHash, sHash, base = [], [1], [1]

        for i in a:
            result = 1
            maxLen = max(maxLen, len(i))
            for j in i:
                result = (result * seed + ord(j) - ord('a')) % mod
            aHash.append(result)

        maxLen, result = max(maxLen, len(s)), 1
        for i in s:
            result = (result * seed + ord(i) - ord('a')) % mod
            sHash.append(result)

        result = 1
        for i in range(maxLen):
            result = result * seed % mod
            base.append(result)

        result = [i for i in s]

        i = 0
        while i < len(s):
            maxLen, index = -1, 0
            for j in range(len(a)):
                size_aj = len(a[j])
                left, right = i + 1, i + size_aj
                if right > len(s):
                    continue

                sHashValue = (sHash[right] - base[right - left + 1] * sHash[left - 1] % mod + mod) % mod
                aHashValue = (aHash[j] - base[size_aj] + mod) % mod
                if  sHashValue == aHashValue and size_aj > maxLen:
                    maxLen = size_aj
                    index = j

            if maxLen != -1:
                for j in range(maxLen):
                    result[i + j] = b[index][j]
                i += maxLen - 1
            i += 1

        return "".join(result)
