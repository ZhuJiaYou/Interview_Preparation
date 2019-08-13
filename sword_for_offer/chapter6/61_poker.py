def is_continuous(nums):
    jokers = nums.count(0)
    cards_left = sorted(nums)[jokers:]
    jokers_need = 0
    for i in range(1, len(cards_left)):
        if cards_left[i] == cards_left[i-1]:
            return False
        jokers_need += cards_left[i] - cards_left[i-1] - 1
    return jokers_need <= jokers


if __name__ == '__main__':
    nums = [0, 0, 1, 2, 3]
    print(is_continuous(nums))
    nums2 = [3, 4, 6, 8, 0]
    print(is_continuous(nums2))
