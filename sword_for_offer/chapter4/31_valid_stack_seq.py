def validate_stack_sequences(pushed: 'list[int]', popped: 'list[int]') -> bool:
    l_ = len(pushed)
    if l_ < 3:
        return True
    for i in range(0, l_-2):
        first = pushed.index(popped[i])
        for j in range(i+1, l_-1):
            second = pushed.index(popped[j])
            if second >= first:
                continue
            for k in range(j+1, l_):
                third = pushed.index(popped[k])
                if third > second and third < first:
                    return False
                print(first, second, third)
    return True


def validate_stack_sequences2(pushed: 'list[int]', popped: 'list[int]') -> bool:
    stack = []
    j = 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return j == len(popped)




if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    popped = [4, 5, 3, 2, 1]
    print(validate_stack_sequences2(pushed, popped))
