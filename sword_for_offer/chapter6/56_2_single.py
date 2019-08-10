def single_num(nums):
    ans = 0
    for i in range(32):
        count = 0
        for num in nums:
            if (num >> i) & 1 == 1:
                count += 1
        ans |= (count % 3 != 0) << i
    if ans >= 2**31:
        ans -= 2**32
    return ans


def single_num2(nums):
    singles = set(nums)
    return (sum(singles)*3 - sum(nums)) // 2


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 1, 1, 4, 4, 4]
    print(single_num2(nums))
