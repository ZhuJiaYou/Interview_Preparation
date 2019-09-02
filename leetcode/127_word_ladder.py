from sys import maxsize
from collections import deque


def ladder_len(begin_word, end_word, words):
    if end_word not in words:
        return 0
    if begin_word in words:
        return 1
    words.append(begin_word)
    graph = [[0]*len(words) for _ in range(len(words))]
    path = [0] * len(words)
    diff = 0
    k = 0
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            for ci, cj in zip(words[i], words[j]):
                if ci != cj:
                    diff += 1
            if diff == 1:
                graph[i][j], graph[j][i] = 1, 1
            diff = 0
    # BFS
    visited = [False] * len(words)
    q = deque()
    q.append(len(words)-1)
    visited[-1] = True
    now = -1
    while q:
        now = q.popleft()
        for i in range(len(words)):
            if graph[now][i] == 1 and not visited[i]:
                path[i] = path[now] + 1
                visited[i] = True
                q.append(i)
    # print(graph)
    return path[words.index(end_word)]+1


def ladder_len2(begin_word, end_word, words):
    def construct_dict(word_list):
        d = {}
        for word in word_list:
            for i in range(len(word)):
                s = word[:i] + '_' + word[i+1:]
                d[s] = d.get(s, []) + [word]
        return d

    def bfs_words(begin, end, dict_words):
        que, visited = deque([(begin, 1)]), set(begin)
        if begin == end:
            return 1
        while que:
            word, steps = que.popleft()
            for i in range(len(word)):
                s = word[:i] + '_' + word[i+1:]
                neighs = dict_words.get(s, [])
                for neigh in neighs:
                    if neigh not in visited:
                        if neigh == end:
                            return steps+1
                        que.append((neigh, steps+1))
                        visited.add(neigh)
        return 0

    if end_word not in words:
        return 0
    d = construct_dict(set(words) | set([begin_word, end_word]))
    return bfs_words(begin_word, end_word, d)


if __name__ == '__main__':
    begin_word = "hit"
    end_word = "cog"
    words = ["hot", "dot", "dog", "lot", "log"]
    print(ladder_len2(begin_word, end_word, words))
