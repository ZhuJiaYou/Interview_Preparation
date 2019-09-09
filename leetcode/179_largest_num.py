from functools import cmp_to_key
def largest_num(nums):
    def cmp(x, y):
        # print(x, y)
        L = min(len(x), len(y))
        # print(L)
        if x[:L] > y[:L]:
            return 1
        elif x[:L] < y[:L]:
            return -1
        else:
            if len(x) == len(y):
                return 0
            elif (len(x)>len(y) and cmp(x[L:], y)>=0) or (len(x)<len(y) and cmp(x, y[L:])>=0):
                return 1
            else:
                return -1

    nums = [str(n) for n in nums]
    nums.sort(key=cmp_to_key(cmp), reverse=True)
    if nums[0] == "0":
        return "0"
    print(nums)
    return "".join(nums)


def largest_num2(nums):
    def cmp(x, y):
        if x+y > y+x:
            return 1
        elif x+y < y+x:
            return -1
        else:
            return 0    

    nums = [str(n) for n in nums]
    nums.sort(key=cmp_to_key(cmp), reverse=True)
    if nums[0] == "0":
        return "0"
    print(nums)
    return "".join(nums)


if __name__ == '__main__':
    nums = [3,30,34,5,9]
    # nums = [0, 0]
    nums = [1440,7548,4240,6616,733,4712,883,8,9576]
    print(largest_num2(nums))
