def verify_bitree_post_retrieve(seq):
    if seq == []:
        return True
    """
    i = 0
    while(i < len(seq) - 1):
        if seq[i] > seq[-1]:
            break
        i += 1
    i -= 1
    """
    # print(seq)
    if len(seq) == 1:
        i = 0
    for i in range(len(seq) - 1):
        if seq[i] > seq[-1]:
            break
    for j in range(i + 1, len(seq) - 1):
        # print(seq[i], seq[j])
        if seq[j] < seq[-1]:
            return False
    # print("aaa")
    return verify_bitree_post_retrieve(seq[:i]) and verify_bitree_post_retrieve(seq[i:-1])


if __name__ == '__main__':
    print(verify_bitree_post_retrieve([5, 7, 6, 9, 11, 10, 8]))
    print(verify_bitree_post_retrieve([4, 6, 7, 5]))
    print(verify_bitree_post_retrieve([7, 4, 6, 5]))
