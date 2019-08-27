def jump_game(nums):
    m = nums[0]
    for i in range(1, len(nums)):
        if i > m:
            return False
        m = max(m, i+nums[i])
    return True


if __name__ == '__main__':
    print(jump_game([2, 3, 1, 1, 4]))
    print(jump_game([3, 2, 1, 0, 4]))
