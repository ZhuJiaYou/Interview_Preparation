from collections import Counter
from fractions import gcd


# WRONG ANSWER
def max_points_w(points):
    if not points:
        return 0
    if len(points) == 1:
        return 1
    lines = []
    line = []
    for i in range(len(points)):
        for j in range(len(points)):
            line.append([-float('inf'), -float('inf')])
        lines.append(line[:])
        line = []

    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            if points[i][0] == points[j][0]:
                lines[i][j] = [float('inf'), points[i][0]]
                lines[j][i] = [float('inf'), points[i][0]]
            else:
                k = (points[i][1]-points[j][1]) / (points[i][0]-points[j][0])
                b = (points[i][0]*points[j][1]-points[j][0]*points[i][1]) / (points[j][0]-points[i][0])
                lines[i][j] = [k, b]
                lines[j][i] = [k, b]
    max_p = 0
    for ls in lines:
        #print(ls)
        ls = [tuple(li) for li in ls]
        maxi = max(Counter(ls).values())
        if maxi > max_p:
            max_p = maxi
    # print(lines)
    return max_p + 1


def max_points(points):
    max_p = 0
    for p in points:
        selfs = 0
        counter = Counter()
        for q in points:
            x, y = q[0]-p[0], q[1]-p[1]
            selfs += ((x==0) and (x==y))
            g = gcd(x, y)
            counter[(y/g, x/g) if x else 'inf'] += 1
        counter['inf'] -= selfs
        max_p = max(max_p, max(counter.values())+selfs)
    return max_p


if __name__ == '__main__':
    # points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    # print(max_points(points))
    # points = [[1, 1], [2, 2], [3, 3]]
    points = [[1, 1], [1, 1], [2, 2], [2, 2]]
    print(max_points(points))
