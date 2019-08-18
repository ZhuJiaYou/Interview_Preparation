def letter_combination(digits):
    d = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    letters = [''] if digits else []
    for c in digits:
        letters = [p+q for p in letters for q in d[int(c)]]
    return letters


def letter_combination2(digits):
    if not digits:
        return []
    d = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    letters = []
    def make(i, current):
        if i == len(digits):
            letters.append(current)
        else:
            for c in d[int(digits[i])]:
                make(i+1, current+c)
    make(0, '')
    return letters


if __name__ == '__main__':
    print(letter_combination('236'))
    print(letter_combination2('236'))
