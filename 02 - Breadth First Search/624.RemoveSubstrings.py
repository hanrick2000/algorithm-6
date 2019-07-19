class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        queue, hash = collections.deque([s]), set([s])

        min_size = len(s)
        while queue:
            s = queue.popleft()
            for sub in dict:
                found_index = s.find(sub)
                while found_index != -1:
                    new_s = s[:found_index] + s[found_index + len(sub):]
                    if new_s not in hash:
                        queue.append(new_s)
                        hash.add(new_s)
                        min_size = min(min_size, len(new_s))

                    found_index = s.find(sub, found_index + 1)

        return min_size
