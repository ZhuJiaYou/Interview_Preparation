from functools import cmp_to_key


def min_num(numbers):
    def my_cmp(x, y):
        if x + y < y + x:
            return -1
        elif x + y > y + x:
            return 1
        else:
            return 0

    return ''.join(sorted([str(i) for i in numbers], key=cmp_to_key(my_cmp)))


if __name__ == '__main__':
    nums = [3, 32, 321]
    print(min_num(nums))
