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


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.start_with("app"))
    trie.insert("app")
    print(trie.search("app"))
