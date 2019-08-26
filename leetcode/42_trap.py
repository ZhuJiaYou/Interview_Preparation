def trap(height):
    waterlevels = []
    left = 0
    for h in height:
        left = max(left, h)
        waterlevels.append(left)
    right = 0
    for i in range(len(height)-1, -1, -1):
        right = max(right, height[i])
        print(right)
        waterlevels[i] = min(waterlevels[i], right) - height[i]
    print(waterlevels)
    return sum(waterlevels)


if __name__ == '__main__':
    nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(nums))
