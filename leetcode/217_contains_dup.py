def contains_num(nums):
    return len(nums) != len(set(nums))


if __name__ == '__main__':
    nums = [1,2,3,1]
    print(contains_num(nums))
