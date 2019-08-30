def largest_rectangle_area(heights):
    largest = 0
    def largest_n(i):
        low, high = i, i
        while low-1 >= 0 and heights[low-1] >= heights[i]:
            low -= 1
        while high+1 < len(heights) and heights[high+1] >= heights[i]:
            high += 1
        return (high-low+1)*heights[i]
    for i in range(len(heights)):
        li = largest_n(i)
        if li > largest:
            largest = li 
    return largest


def largest_rectangle_area2(heights):
    heights.append(0)
    left_boundries = [-1]
    largest = 0
    for i in range(len(heights)):
        while heights[i] < heights[left_boundries[-1]]:
            h = heights[left_boundries.pop()]
            w = i - left_boundries[-1] - 1
            largest = max(largest, w*h)
        left_boundries.append(i)
    print(heights)
    print(left_boundries)
    return largest



if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    print(largest_rectangle_area(heights))
    print(largest_rectangle_area2(heights))
