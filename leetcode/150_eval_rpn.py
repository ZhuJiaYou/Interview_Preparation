from operator import add, sub, mul


def eval_rpn(tokens):
    def truncate_div(op1, op2):
        flag = False
        if op1 == 0:
            return 0
        if (op1>0 and op2>0) or (op1<0 and op2<0):
            flag = True
        res = abs(op1) // abs(op2)
        return res if flag else -res

    operands = []
    rands = "+-*/"
    rand_dicts = {'+':add, '-':sub, '*':mul, '/':truncate_div}
    for tok in tokens:
        if tok in rands:
            op2 = operands.pop()
            op1 = operands.pop()
            operands.append(rand_dicts[tok](op1, op2))
        else:
            operands.append(int(tok))
    return operands[-1]





if __name__ == '__main__':
    rpn = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    # rpn = ["2", "1", "+", "3", "*"]
    # rpn = ["4", "13", "5", "/", "+"]
    print(eval_rpn(rpn))
