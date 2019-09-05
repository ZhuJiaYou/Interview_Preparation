def word_break(s, words):
    sentences = []
    def dfs(sentence, start):
        if start == len(s):
            sentences.append(sentence.strip())
        for j in range(start+1, len(s)+1):
            if s[start:j] in words:
                dfs(sentence+s[start:j]+" ", j)
    dfs("", 0)
    return(sentences)


def word_break2(s, words):
    sentences = []
    paths = [[] for _ in range(len(s)+1)]
    paths[0] = ["True"]
    max_word_len = max([len(w) for w in words+[""]])

    for i in range(1, len(s)+1):
        for j in range(max(0, i-max_word_len), i):
            if paths[j] and s[j:i] in words:
                paths[i].append(s[j:i])
    
    def dfs(end, path):
        if 0 == end:
            sentences.append(path)
            return
        for word in paths[end]:
            if path:
                dfs(end-len(word), word+" "+path)
            else:
                dfs(end-len(word), word)

    dfs(len(s), "")
    return(sentences)



if __name__ == '__main__':
    s = "catsanddog"
    words = ["cat", "cats", "and", "sand", "dog"]
    print(word_break2(s, words))
    s = "pineapplepenapple"
    words = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(word_break2(s, words))
    s = "catsandog"
    words = ["cats", "dog", "sand", "and", "cat"]
    print(word_break2(s, words))
