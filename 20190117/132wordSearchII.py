class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

class Solution:
    def __init__(self):
        self.DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if not board:
            return []

        results, trie = set(), Trie()
        for word in words:
            trie.add(word)

        for i in range(len(board)):
            for j in range(len(board[i])):
                char = board[i][j]
                self.search(board, i, j, trie.root.children.get(char), set([(i, j)]), results)

        return list(results)

    def search(self, matrix, x, y, root, visited, results):
        if not root:
            return

        if root.word is not None:
            results.add(root.word)

        for directionX, directionY in self.DIRECTIONS:
            targetX = x + directionX
            targetY = y + directionY

            if not self.is_valid(matrix, targetX, targetY) or (targetX, targetY) in visited:
                continue

            visited.add((targetX, targetY))
            self.search(matrix, targetX, targetY, root.children.get(matrix[targetX][targetY]), visited, results)
            visited.remove((targetX, targetY))

    def is_valid(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] is not None
