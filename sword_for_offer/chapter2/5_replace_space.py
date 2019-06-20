def replace_space(s: str) -> str:
    # return ''.join(c if c != ' ' else '%20' for c in s)
    return s.replace(' ', '%20')


def replace_space2(s: str) -> str:
    s[0] = '0'
    print(s)



if __name__ == '__main__':
    s = 'We are happy.'
    print(replace_space2(s))
