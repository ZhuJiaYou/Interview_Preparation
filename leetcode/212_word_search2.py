from collections import defaultdict


class TrieNode:
    def __init__(self, exits=False):
        self.exits = exits
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        self.search_root(word, False).exits = True

    def search(self, word):
        child_root = self.search_root(word)
        return child_root and child_root.exits

    def start_with(self, prefix):
        return bool(self.search_root(prefix))

    def search_root(self, word, should_exist=True):
        root = self.root
        for c in word:
            if should_exist and c not in root.children:
                return False
            root = root.children[c]
        return root


class Solution:
    def find_words(self, board, words):
        if not board or not words:
            return []
        trie = Trie()
        for w in words:
            trie.insert(w)
        res = set()
        visited = [[False]*len(board[0]) for _ in range(len(board))]

        def dfs(i, j, now):
            if trie.search(now):
                # print(res)
                res.add(now)
            for i, j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0<=i<len(board) and 0<=j<len(board[0]) and not visited[i][j]:
                    now += board[i][j]
                    visited[i][j] = True
                    if trie.start_with(now):
                        dfs(i, j, now)
                    now = now[:-1]
                    visited[i][j] = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited[i][j] = True
                dfs(i, j, board[i][j])
                visited[i][j] = False
        return list(res)


if __name__ == '__main__':
    sln = Solution()
    board = [
             ['o','a','a','n'],
             ['e','t','a','e'],
             ['i','h','k','r'],
             ['i','f','l','v']
            ]
    words = ["oath","pea","eat","rain"]
    board = [["a", "a"]]
    words = ["aaa"]
    print(sln.find_words(board, words))
