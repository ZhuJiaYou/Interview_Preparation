def generate_parenthesis(n):
    parens = []
    def generate(left_num, right_num, paren):
        if left_num == n and right_num == n:
            parens.append(paren)
        if left_num < n:
            generate(left_num+1, right_num, paren+'(')
        if right_num < n and right_num < left_num:
            generate(left_num, right_num+1, paren+')')
    generate(0, 0, '')
    return parens


if __name__ == '__main__':
    print(generate_parenthesis(3))
