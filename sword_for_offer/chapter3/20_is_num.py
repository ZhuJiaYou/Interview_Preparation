from collections import Counter


def is_num(s):
    s = s.strip()
    valid_chars = "0123456789+-e."
    b = dict(Counter(s))
    for i in range(len(s)):
        if s[i] not in valid_chars:
            return False
        if s[i] == '0':
            if len(s) > 1 and s[0] == '0' and s[1] == '0':
                return False
        if s[i] == '.':
            if b[s[i]] > 1 or (i == 0) or (i == len(s)-1) or (s[i-1] not in valid_chars[:10]) or \
                    (s[i+1] not in valid_chars[:10]):
                return False
        if s[i] == '+' or s[i] == '-':
            if (i!=0 and s[i-1]!='e') or i==len(s)-1 or (s[i+1] not in valid_chars[:10]):
                return False
        if s[i] == 'e':
            if i==0 or i==len(s)-1:
                return False
        # if s[i] == '-':
            # if i!=0 and s[i-1]!=e:
                # return False
    return True


if __name__ == '__main__':
    print(is_num("123"))
    print(is_num("0.1"))
    print(is_num("6e-1"))
    print(is_num("1e"))
    print(is_num("--6"))
