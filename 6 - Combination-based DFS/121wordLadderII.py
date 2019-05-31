class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)

        indexs = self.build_indexes(dict)

        distances = {}
        self.bfs(end, start, distances, indexs)

        results = []
        self.dfs(start, end, distances, indexs, [start], results)

        return results

    def build_indexes(self, dict):
        results = {}
        for word in dict:
            for i in range(len(word)):
                key = word[:i] + '%' + word[i + 1:]
                if key in results:
                    results[key].add(word)
                else:
                    results[key] = set([word])
        return results

    def bfs(self, end, start, distances, indexs):
        distances[start] = 0
        queue = collections.deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, indexs):
                if next_word not in distances:
                    distances[next_word] = distances[word] + 1
                    queue.append(next_word)

    def get_next_words(self, word, indexs):
        results = []

        for i in range(len(word)):
            key = word[:i] + '%' + word[i + 1:]
            for aword in indexs.get(key, []):
                results.append(aword)

        return results

    def dfs(self, start, end, distances, indexs, paths, results):
        if start == end:
            results.append(list(paths))
            return

        for next_word in self.get_next_words(start, indexs):
            if distances[next_word] != distances[start] + 1:
                continue

            paths.append(next_word)
            self.dfs(next_word, end, distances, indexs, paths, results)
            paths.pop()
