from functools import reduce
from operator import xor


def single_num(nums):
    return reduce(xor, nums)


if __name__ == '__main__':
    nums = [2, 2, 1]
    print(single_num(nums))
    nums = [4, 1, 2, 2, 1]
    print(single_num(nums))
