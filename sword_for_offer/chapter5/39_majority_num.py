def majority_element(a):
    count = 0
    p = None
    for i in a:
        if count == 0:
            p = i
            count += 1
        else:
            if i == p:
                count += 1
            else:
                count -= 1
    return p


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(majority_element(nums))
