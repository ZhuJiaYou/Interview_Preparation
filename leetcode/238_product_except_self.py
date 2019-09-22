def product_except_self(nums):
    now = 1
    output = []
    for i in range(len(nums)):
        output.append(now)
        now = nums[i] * now
    now = 1
    for i in range(len(nums)-1, -1, -1):
        output[i] *= now
        now *= nums[i]
    return output


if __name__ == '__main__':
    nums = [1,2,3,4]
    print(product_except_self(nums))
